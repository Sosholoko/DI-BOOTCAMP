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


def load_json():
    # filename = os.path.join(basedir, "Week 12:4/Project/webapp/static/users.json")
    # f = open(filename, 'r')
    # users = json.load(f)
    # f.close()

    # return users

    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    return users

def populate(db):
    users = load_json()
    
    for user in users:
        user_obj = models.Users(
            name = user["name"],
            street = user["address"]['street'],
            city = user["address"]["city"],
            zipcode = user["address"]["zipcode"]
            
        )

        db.session.add(user_obj)
        print(f"Added {user['name']} to the DB !")

        db.session.commit()


populate(db)


