from http import client
from flask import Flask, render_template, Blueprint
import json
import socket
import threading
import sys
from flask_socketio import SocketIO

with open('config.json', 'r') as f:
    data = json.load(f)

home = Blueprint('home', __name__)

@client.route("/")
def homepage():
    return render_template('src/index.html', data=data)


# app = Flask(__name__)
# app.config.from_pyfile('settingslocal.py')
# app.register_blueprint(home)
# socketio = SocketIO(app)

ip = data["ip"]
port = data["port"]
extension = data["extension"]

def createApp(config_file):
    app = Flask(__name__) #Create application object
    app.config.from_pyfile(config_file) # Configure application with settings file
    app.register_blueprint(home) # Register urls so application knows what to do
    app = SocketIO(app)    
    return app

if __name__ == '__main__':
    app = createApp('settingslocal.py') # Create application with the config file
    app.run()
