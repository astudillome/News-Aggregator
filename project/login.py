from flask import Flask
from flask.json import load
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from project.models import User
from project.app import app

if __name__ == '__main__':
  
  # app.config['SECRET_KEY'] = "dunno what you know if you know what i mean"

  # login_manager = LoginManager()
  # login_manager.init_app(app)
  # login_manager.login_view = 'login'

  # app.run(debug = DEBUG, host=HOST, port= PORT)