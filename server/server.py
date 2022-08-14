import os
from datetime import datetime

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

clients = 0


@app.route('/start')
def send():
    socketio.emit('start')
    return "<p>Started process on {} client(s)</p>".format(clients)


@app.route('/')
def home():
    return "<p>There are {} connected clients</p><a href='/start'>Start</a>".format(clients)


socketio = SocketIO(app)


@socketio.on('file')
def handle_message(data):
    directory = create_dir()
    file = open(os.path.join(directory, "{}_{}".format(data['client'], data['file'])), "w")
    file.write(data['data'])
    file.close()


def create_dir():
    cwd = os.getcwd()
    directory = os.path.join(cwd, "output")
    if not os.path.exists(directory):
        os.mkdir(directory)
    now = datetime.now()

    directory = os.path.join(cwd, "output", str(now.strftime("%d-%m-%Y_%H-%M-%S")))
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory


@socketio.on('connect')
def connect():
    global clients
    clients += 1


@socketio.on('disconnect')
def disconnect():
    global clients
    clients -= 1


socketio.run(app)
