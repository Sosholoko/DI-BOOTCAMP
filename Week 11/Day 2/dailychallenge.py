import flask
from flask import request, session, redirect, url_for, g
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     def __repr__(self):
#         return f'<User : {self.username}>'


# users = []
# users.append(User(id=1, username = "Sasha", password = 'sasha'))
# users.append(User(id=2, username = "Shirel", password = 'shirel'))

# print(users)


app = flask.Flask(__name__)
app.secret_key = "secretkey"


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField("Email", [validators.Length(min=6, max=50)])
    password = StringField("Password", [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Password does not match")
        ])
    confirm : PasswordField('Confirm Password')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        return render_template('register.html')
    return flask.render_template('register.html', form=form)



# @app.before_request
# def before_request():
#     if "user_id" in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.pop("user_id", None)

#         username = request.form['username']
#         password = request.form['password']

#         user = [x for x in users if x.username == username][0]
#         if user and user.password == password:
#             session['user_id'] = user.id
#             return redirect(url_for('profile'))

#         return redirect(url_for("login"))

#     return flask.render_template('login.html')

# @app.route('/profile')
# def profile():
#     return flask.render_template("profile.html")


app.run(debug = True)