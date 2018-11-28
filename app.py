import random
import json
from flask import Flask, request, abort, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

button_types = ['DOUBLE', 'SINGLE', 'LONG']




class ButtonStatus(object):
    def __init__(self):
        self.status = []
        # Gen a random code to check against
        self.code = []
        self.newCode()

    def newCode(self, count=3):
        self.code = []
        for i in range(count):
            self.code.append(random.choice(button_types))
        self.log("Generated new code:", self.code)
        self.status = []
    
    def update(self, value):
        if value in button_types:
            self.status.append(value)
            if len(self.status) > 3:
                self.status = self.status[-3:]
            self.log("Status of the presses:", self.status)
            return True
        return False

    def getStatus(self):
        status = []
        for i in range(len(self.code)):
            j = {'value': self.code[i]}
            try:
                x = self.status[i]
            except IndexError:
                x = None
            j['authed'] = x == self.code[i]
            status.append(j)
        authed = all(j['authed'] for j in status)
        print("not authed")
        print(json.dumps(status))
        return authed, status
    
    def log(self, *args, **kwargs):
        print(*args, **kwargs)

@app.route('/')
def hello_world():
    is_authed, status = BUTTON_STATUS.getStatus()
    if is_authed:
        BUTTON_STATUS.newCode()  # Regen the code
        return render_template("success.html")
    return render_template('login.html', status=status)


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
        #return str(request.args)
        try:
            global BUTTON_PUSHED
            val = BUTTON_STATUS.update(request.args['value'])
            return json.dumps({'status': val})
        except:
            pass
    return '{"status":"False"}\n'
    abort(404)

if __name__ == '__main__':
    global BUTTON_STATUS
    BUTTON_STATUS = ButtonStatus()
    app.run(host='0.0.0.0', debug=True)
