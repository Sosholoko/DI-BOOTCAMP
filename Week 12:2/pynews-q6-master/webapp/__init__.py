import os
import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
from flask_socketio import SocketIO, emit, send
import pusher
from time import localtime, strftime


app = flask.Flask(__name__)





basedir = os.path.abspath(os.path.dirname(__file__))
# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "my-very-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
socketio = SocketIO(app, cors_allowed_origins="*")


# Format of a postgresSQL database url:
# postgresql://<username>:<password>@<hostname>:<port>/<db_name>
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/pynews"
db = flask_sqlalchemy.SQLAlchemy(app)    # database bridge
migrate = flask_migrate.Migrate(app, db) # Migrator
login_manager = flask_login.LoginManager(app)
if __name__ == '__main__':
    socketio.run(app, debug=True)

from . import routes, models

