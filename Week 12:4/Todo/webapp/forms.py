import flask_wtf
import wtforms

class AddTodoForm(flask_wtf.FlaskForm):

    details = wtforms.StringField("To Do")
    submit = wtforms.SubmitField("Add")
