from . import db, login_manager # Database bridge created in __init__.py
import flask_login

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class Todo(db.Model, flask_login.UserMixin): # db.Model is required if you want to create an SQL model

    # Every attribute is a class variable

    id = db.Column(db.Integer(), primary_key=True)

    task = db.Column(db.String(64))
    
