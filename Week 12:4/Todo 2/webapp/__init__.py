import os
import json
import flask
import flask_sqlalchemy, flask_migrate, requests





app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "thisisaverysecretKEY"


# __file__ is __init__.py --> Here it's special bc __init__.py is actually webapp/
# >>> __file__ is webapp <<<


basedir = os.path.abspath(os.path.dirname(__file__)) # import os !
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/airline"

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app=app, db=db)




from . import models, routes