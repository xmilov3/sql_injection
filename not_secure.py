from flask import Flask, request, send_from_directory
import mysql.connector

def execute_query(query):
    try:
        connection = mysql.connector.connect(
            host='localhost',     
            user='root',          
            password='',          
            database='bsui_lab06' 
        )
        cursor = connection.cursor(dictionary=True)  
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
    return send_from_directory('.', 'test_form_not_secured.html')

@app.route('/login', methods=['POST'])
def login_unsecured():
    username = request.form['username']
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = execute_query(query)
    if result:
        return "Logged in!"
    else:
        return "Invalid credentials"


if __name__ == '__main__':
    app.run(debug=True)
