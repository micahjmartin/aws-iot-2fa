from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


global BUTTON_PUSHED

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


@app.route('/button', methods=["POST"])
def button_login():
    if request.method == "POST":
        data = request.json
        if data:
            global BUTTON_PUSHED
            BUTTON_PUSHED = data.get("clickType", None)

if __name__ == '__main__':
    socketio.run(app)

