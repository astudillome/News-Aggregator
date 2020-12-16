from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
  
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/news_dev'
app.config['SECRET_KEY'] = "dunno what you know if you know what i mean"
  
db.init_app(app)

if __name__ == "__main__":
    app.run()