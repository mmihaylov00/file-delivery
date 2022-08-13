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
socketio = SocketIO(app)

@app.route('/')
def homepage():
    return render_template('src/index.html', data=data)

ip = data["ip"]
port = data["port"]
extension = data["extension"]

if __name__ == '__main__':
    socketio.run(app)