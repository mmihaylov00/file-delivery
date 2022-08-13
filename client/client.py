from http import client
from flask import Flask, render_template
from home.views import home_view
import json
import socket, threading, sys

with open('config.json','r') as f:
    data =json.load(f)

s = socket.socket()
host = socket.gethostname()

port = 5000

@client.route("/")
def homepage():
    return render_template('index.html', data=data)




# def createApp(config_file):
#     app = Flask(__name__) #Create application object
#     app.config.from_pyfile(config_file) # Configure application with settings file
#     app.register_blueprint(home_view) # Register urls so application knows what to do
#     return app

if __name__=='__main__':
    app = Flask(__name__) 
    #app = createApp('settingslocal.py') # Create application with the config file
    app.run()