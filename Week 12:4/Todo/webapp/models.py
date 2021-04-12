from . import db

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.Text)
    due_date = db.Column(db.DateTime())