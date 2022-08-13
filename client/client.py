from flask import Flask
from home.views import home_view

def createApp(config_file):
    app = Flask(__name__) #Create application object
    app.config.from_pyfile(config_file) # Configure application with settings file
    app.register_blueprint(home_view) # Register urls so application knows what to do
    return app

if __name__=='__main__':
    app = createApp('settingslocal.py') # Create application with the config file
    app.run()