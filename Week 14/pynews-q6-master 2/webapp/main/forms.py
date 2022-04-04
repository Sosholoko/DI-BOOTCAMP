import flask_wtf
import wtforms
from wtforms import validators as vld

# Form class --> flask_wtf.FlaskForm
# Form fields --> wtforms.SomethingField

# each form is a class inheriting from flask_wtf.FlaskForm
# every class attribute is a field in the form

class QueryForm(flask_wtf.FlaskForm):

    query = wtforms.StringField("Query: ", validators=[vld.DataRequired(message="Input something..")])

    submit = wtforms.SubmitField("Search")


class SignUpForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ", validators=[vld.Length(6, 12)])

    submit = wtforms.SubmitField("Sign up")

class SignInForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ", validators=[vld.Length(6, 12)])

    submit = wtforms.SubmitField("Sign in")