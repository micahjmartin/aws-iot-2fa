from flask import Flask, request
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


global BUTTON_PUSHED

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/button', methods=["POST"])
def button_login():
    if request.method == "POST":
        data = request.json
        if data:
            global BUTTON_PUSHED
            BUTTON_PUSHED = data.get("clickType", None)

if __main__ == __name__:
    socketio.run(app)
