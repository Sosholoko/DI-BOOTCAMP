from . import app, db
from . import models
import flask
from flask import redirect, url_for, request


@app.route("/")
def home():
    todos = models.Todo.query.filter_by(complete = False).all()
    todoc = models.Todo.query.filter_by(complete = True).all()
    return flask.render_template("index.html", todos = todos, todoc = todoc)

@app.route("/add", methods =["POST"])
def add():
    todo = models.Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('home'))

@app.route("/update/<id>")
def update(id):
    
    todo = models.Todo.query.filter_by(id = int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/delete/<int:id>")
def delete(id):
    todel = models.Todo.query.get_or_404(id)

    try:
        db.session.delete(todel)
        db.session.commit()
        return redirect('/')
    except:
        return "Problem encountered during deleting process"