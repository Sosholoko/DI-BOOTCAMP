import os

basedir = os.path.abspath(os.path.dirname(__file__))


# https://flask.palletsprojects.com/en/1.1.x/config/
class Config:

    DEBUG = True
    SECRET_KEY = "my-very-secret-key"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    BASEDIR = basedir

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = "mikefisher0408@gmail.com"
    MAIL_PASSWORD = "zafsaaeklnwuzofu"
    MAIL_DEFAULT_SENDER = "mikefisher0408@gmail.com"

class PostgresConfig(Config):

    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@localhost:5432/pynews"



configs = {
    "basic": Config,
    "postgres": PostgresConfig,
}

current_config = configs["basic"] # Replace with input ?
