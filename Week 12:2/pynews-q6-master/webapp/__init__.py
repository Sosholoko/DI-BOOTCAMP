import os
import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
from flask_socketio import SocketIO, emit, send
import pusher
from time import localtime, strftime
import flask_mail



app = flask.Flask(__name__)





basedir = os.path.abspath(os.path.dirname(__file__))
# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "my-very-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
    
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.config['MAIL_USERNAME'] = "deadsnake555@gmail.com"
app.config['MAIL_PASSWORD'] = "ztlqtktcqgytgvvd"
app.config['MAIL_DEFAULT_SENDER'] = "deadsnake555@gmail.com"


socketio = SocketIO(app, cors_allowed_origins="*")


db = flask_sqlalchemy.SQLAlchemy(app)    # database bridge
migrate = flask_migrate.Migrate(app, db) # Migrator
login_manager = flask_login.LoginManager(app)
mail_manager = flask_mail.Mail(app)


if __name__ == '__main__':
    socketio.run(app, debug=True)

from . import routes, models, filters





