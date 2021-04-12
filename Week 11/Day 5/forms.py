import wtforms
import flask_wtf
from wtforms import validators as vld

#Form class

class TestForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name: ") 
    age = wtforms.IntegerField("Age: ")

    submit = wtforms.SubmitField("Submit")

class LoginForm(flask_wtf.FlaskForm):

    user = wtforms.StringField("Username ")
    passw = wtforms.PasswordField("Password ", validators=[vld.Length(6, 12)])

    connect = wtforms.SubmitField("Connect")
