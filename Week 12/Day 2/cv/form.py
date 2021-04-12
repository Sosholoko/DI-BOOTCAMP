import wtforms
import flask_wtf
from wtforms import validators as vld


class CvForm(flask_wtf.FlaskForm):

    firstname = wtforms.StringField("First Name: ", validators=[vld.DataRequired(message="Input something..")]) 
    lastname = wtforms.StringField("Last Name: ", validators=[vld.DataRequired(message="Input something..")]) 
    age = wtforms.IntegerField("Age: ", validators=[vld.DataRequired(message="Input something..")])
    phone = wtforms.IntegerField("Phone Number: ", validators=[vld.DataRequired(message="Input something..")])
    email = wtforms.StringField("Email Adress: ", validators=[vld.DataRequired(message="Input something..")])
    city = wtforms.StringField("Living City: ", validators=[vld.DataRequired(message="Input something..")])
    actwork = wtforms.StringField("Actual Work : ", validators=[vld.DataRequired(message="Input something..")])
    social1 = wtforms.StringField("Facebook: ", validators=[vld.DataRequired(message="Input something..")])
    social2 = wtforms.StringField("Linkdin: ", validators=[vld.DataRequired(message="Input something..")])
    prof = wtforms.StringField("Profile ",validators=[vld.DataRequired(message="Input something..")])
    date = wtforms.StringField("Career Date 1)", validators=[vld.DataRequired(message="Input something..")])
    date1 = wtforms.StringField("Career Date 2)", validators=[vld.DataRequired(message="Input something..")])
    date2 = wtforms.StringField("Career Date 3)", validators=[vld.DataRequired(message="Input something..")])
    date3 = wtforms.StringField("Career Date 4)", validators=[vld.DataRequired(message="Input something..")])
    skill = wtforms.StringField("Skills :", validators=[vld.DataRequired(message="Input something..")])
    skill1 = wtforms.StringField("Skills :", validators=[vld.DataRequired(message="Input something..")])
    skill2 = wtforms.StringField("Skills :", validators=[vld.DataRequired(message="Input something..")])


    submit = wtforms.SubmitField("Submit")


class LoginForm(flask_wtf.FlaskForm):
    
    user = wtforms.StringField("Username ")
    email = wtforms.StringField("Email")
    passw = wtforms.PasswordField("Password ", validators=[vld.Length(6, 12)])

    connect = wtforms.SubmitField("Sign In")



