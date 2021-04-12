import flask

from . import models
from . import app, db

@app.route("/")
def todo_list():
    todos = models.Todo.query.all()

    return flask.render_template("index.html")


@app.route("/add-todo")
def add_todo():
    form = form.AddTodoForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            details = form.details.data

            todo = models.Todo(details=details)
            db.session.add(todo)
            db.commit()
        else:
            print("Something went wrong", form.errors)
    
    return flask.render_template("add_todo.html", form=form)