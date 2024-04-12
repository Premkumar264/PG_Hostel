import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app, support_credentials=True)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Prem@2604",
    host="localhost"
)
cursor = conn.cursor(cursor_factory=RealDictCursor)

# API to authenticate user
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Query the database for the provided student_id
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user:

        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful',
                            'isValid': True,
                            }
                           )
        else:
            return jsonify({'message': 'Invalid Credentials'}), 401
    else:
        return jsonify({'message': 'user not found'}), 404
        
# API to list all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return jsonify({'results': students})




  
# API to add user details
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.json
        cursor.execute("INSERT INTO students (student_id, module, first_name, last_name, mail_id, mobile, country, parent_name, block_name, room_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (data.get('student_id'), data.get('module'), data.get('first_name'), data.get('last_name'), data.get('mail_id'), data.get('mobile'), data.get('country'), data.get('parent_name'), data.get('block_name'), data.get('room_no')))
        conn.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except psycopg2.Error as e:
        print("Error inserting data into database:", e)
        return jsonify({'message': 'Internal Server Error'}), 500

# API to delete user
@app.route('/users/<string:student_id>', methods=['DELETE'])
def delete_user(student_id):
    try:
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        return jsonify({'message': 'User deleted successfully'})
    except psycopg2.Error as e:
        print("Error deleting data from database:", e)
        return jsonify({'message': 'Internal Server Error'}), 500


# API to edit details of the student
@app.route('/user/<string:student_id>', methods=['PUT'])
def update_user(student_id):
    data = request.json
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()
    if student:
        update_query = """
            UPDATE students 
            SET module = %s, 
                first_name = %s, 
                last_name = %s, 
                mail_id = %s, 
                mobile = %s, 
                country = %s, 
                parent_name = %s, 
                block_name = %s, 
                room_no = %s 
            WHERE student_id = %s
        """
        try:
            cursor.execute(update_query, (
                data.get('module', student['module']),
                data.get('first_name', student['first_name']),
                data.get('last_name', student['last_name']),
                data.get('mail_id', student['mail_id']),
                data.get('mobile', student['mobile']),
                data.get('country', student['country']),
                data.get('parent_name', student['parent_name']),
                data.get('block_name', student['block_name']),
                data.get('room_no', student['room_no']),
                student_id
            ))
            conn.commit()
            return jsonify({'message': 'Student details updated successfully'})
        except psycopg2.IntegrityError:
            conn.rollback()
            return jsonify({'message': 'Error: Could not update student details. Student ID already exists'}), 400
    else:
        return jsonify({'message': 'Student not found'}), 404
   

if __name__ == '__main__':
    app.run(debug=True)
