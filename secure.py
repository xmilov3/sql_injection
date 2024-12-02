from flask import Flask, request, send_from_directory
import mysql.connector

def execute_query(query, params=None):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bsui_lab06'
        )
        cursor = connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve_html():
    return send_from_directory('.', 'test_form.html')

@app.route('/login-secured', methods=['POST'])
def login_secured():
    username = request.form['username']
    password = request.form['password']
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    result = execute_query(query, (username, password))
    if result:
        return "Logged in!"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)
