from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if user == "dad" and password == "password":
            return "User logged in, issue a cookie"
        return "User not authorized (will redirect back to login page)"
    else:
        return "Login page goes here"

