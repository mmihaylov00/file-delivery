from http import client
from flask import Flask, render_template, Blueprint
import json
import socket
import threading
import sys
from flask_socketio import SocketIO

with open('config.json', 'r') as f:
    data = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@socketio.route('/')
def homepage():
    return 'asd'#render_template('src/index.html', data=data)

ip = data["ip"]
port = data["port"]
extension = data["extension"]

socketio.run(app)