from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)

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




if __name__ == '__main__':
    app.run(debug=True)
