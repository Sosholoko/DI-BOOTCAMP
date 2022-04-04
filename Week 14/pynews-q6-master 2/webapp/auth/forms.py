import flask_wtf
import wtforms
from wtforms import validators as vld

class SignUpForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    mail     = wtforms.StringField("Mail: ")
    password = wtforms.PasswordField("Password: ", validators=[vld.Length(6, 12)])
    profile_pic = wtforms.FileField("Profile picture:")

    submit = wtforms.SubmitField("Sign up")

class SignInForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ", validators=[vld.Length(6, 12)])

    submit = wtforms.SubmitField("Sign in")

class ResetPasswordForm(flask_wtf.FlaskForm):
    
    password = wtforms.PasswordField("Password: ", validators=[vld.Length(6, 12)])

    submit = wtforms.SubmitField("Reset password")


class ForgotPasswordform(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username: ")

    submit = wtforms.SubmitField("Reset password")




