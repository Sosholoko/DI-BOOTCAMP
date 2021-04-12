from . import app, db
from . import models
import flask

@app.route('/')
def home():

    users = models.Users.query.all()
    return flask.render_template("index.html", users=users)