# MODELS.py
from . import db, login_manager # Database bridge created in __init__.py
import flask_login

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)






class User(db.Model, flask_login.UserMixin): # db.Model is required if you want to create an SQL model

    # Every attribute is a class variable

    id = db.Column(db.Integer(), primary_key=True)

    mail = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    boolean = db.Column(db.Boolean, default=False)



class Message(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50))
    message = db.Column(db.String(500))

class NewMessage(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50))
    message = db.Column(db.String(500))

class Crypto(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    is_active = db.Column(db.Integer())

    # def get_info(crypto_id):
    #     crypto_info = Crypto.query.get(crypto_id)


