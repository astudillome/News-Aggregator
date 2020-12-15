from flask import Flask, g
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
from project.app import app


db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "dunno what you know if you know what i mean"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
  user = User.query.get(int(user_id))
  return user

class User(UserMixin, db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  name = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  archives = db.relationship('Archive', backref='user', lazy=True)

  def __repr__(self):
    return f"User(id={self.id}, email='{self.email}', name='{self.name}', password='{self.password}'"

  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  
class Archive(db.Model):
  __tablename__ = 'archives'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
  article_title = db.Column(db.String, nullable=False)
  article_link = db.Column(db.String, nullable=False)
  comments = db.relationship('Comment', backref='archive', lazy=True)

  def __repr__(self):
    return f"Archive(id={self.id}, article_title='{self.article_title}', article_link='{self.article_link}'"

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  archive_id = db.Column(db.Integer, db.ForeignKey("archives.id", ondelete="SET NULL"))
  name = db.Column(db.String, nullable=False)
  content = db.Column(db.String, nullable=False)
  article_link = db.Column(db.String, nullable=False)
  
  def __repr__(self):
    return f"Comment(id={self.id}, name='{self.name}', content=æ{self.content}', article_link='{self.article_link}'"
  
db.create_all()

