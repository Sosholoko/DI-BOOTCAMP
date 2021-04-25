import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_socketio import SocketIO, join_room, leave_room, send



# Configure app
app = Flask(__name__)
app.config["SECRET_KEY"] = "myverysecretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"


socketio = SocketIO(app)


@app.route('/chat')
def chat():
    return render_template("chat.html")


@socketio.on('message')
def message(data):
    print(f"{data}")
    send(data)

if __name__ == "__main__":
    socketio.run(app, debug=True)