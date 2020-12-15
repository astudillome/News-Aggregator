from flask import Flask
from flask.json import load
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
  
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/news_dev'
app.config['SECRET_KEY'] = "dunno what you know if you know what i mean"
  
db.init_app(app)

if __name__ == "__main__":
    app.run()