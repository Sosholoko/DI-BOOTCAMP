# MODELS.py
import flask_login

from . import db, login_manager  # Database bridge created in __init__.py

# First step:
# Secondary table for the User<>Book ManyToMany relationship
class Quote(db.Model):
    """
    quote
    +-----------+-------------------+--------------------+--------------------+---------------------------------+
    |  id (PK)  |  sentence(str64)  |    author (str64)  |   date (datetime)  |    user_id(int) --> FK to User  |
    +-----------+-------------------+--------------------+--------------------+---------------------------------+
    |           |                   |                    |                    |               3                 |
    +-----------+-------------------+--------------------+--------------------+---------------------------------+
    """

    id = db.Column(db.Integer(), primary_key=True)

    sentence = db.Column(db.String(256), nullable=False)
    author   = db.Column(db.String(64), nullable=True)
    date     = db.Column(db.DateTime(), nullable=True)

    user_id  = db.Column(db.Integer(), db.ForeignKey("user.id"))


class Book(db.Model):

    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(64))

