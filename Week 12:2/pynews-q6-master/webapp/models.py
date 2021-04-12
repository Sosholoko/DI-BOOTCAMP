# MODELS.py
from . import db, login_manager # Database bridge created in __init__.py
import flask_login

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, flask_login.UserMixin): # db.Model is required if you want to create an SQL model

    # Every attribute is a class variable

    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(64))
    password = db.Column(db.String(64))

    fav_quote = db.relationship('Quote', backref="user", uselist = False)


class Quote(db.Model):

    id = db.Column(db.Integer(), primary_key=True)

    sentense = db.Column(db.String(256), nullable = False)
    author = db.Column(db.String(64), nullable = True)
    date = db.Column(db.DateTime(), nullable = True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

class Book(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))
    language = db.Column(db.String(32))

    author_id = db.Column(db.Integer(), db.ForeignKey('human.id'))
    #author = db.relationship('Human', backref="author", uselist = False)

class Human(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))

    written_by = db.relationship('Book', backref="author")



