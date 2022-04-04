import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import flask_mail

import os




db = flask_sqlalchemy.SQLAlchemy()              # database bridge
migrate = flask_migrate.Migrate()               # Migrator
login_manager = flask_login.LoginManager()
mail_manager = flask_mail.Mail()



def create_app(conf):
    from .auth import auth_blueprint
    from .main import main_blueprint

    app = flask.Flask(__name__)

    app.config.from_object(conf)

    db.init_app(app)
    migrate.init_app(db=db, app=app)
    login_manager.init_app(app)
    mail_manager.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
