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


# API to list all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return jsonify({'results': students})




if __name__ == '__main__':
    app.run(debug=True)
