import flask
from .. import db, login_manager, mail_manager

auth_blueprint = flask.Blueprint('auth', __name__)

from . import routes, models # Python needs to read those files !