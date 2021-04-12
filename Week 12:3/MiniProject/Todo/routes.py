import flask

from . import app       # . is webapp/
from . import forms, news_functions, models, db
import flask_login

@app.route("/")
def home():
    return flask.render_template("base.html")