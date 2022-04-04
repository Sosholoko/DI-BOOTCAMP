import flask
from flask import request, jsonify
from flask_socketio import SocketIO, emit, send
from . import app       # . is webapp/
from . import forms, models, db, mail_functions
import flask_login
import pusher
import json
from time import localtime, strftime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects



socketio = SocketIO(app, cors_allowed_origins="*")

pusher_client = pusher.Pusher(
    app_id='1190483',
    key='9282a2def65164d7d0bb',
    secret='5f43b399aac7287fd054',
    cluster='ap2',
    ssl=True
)

@app.route("/test")
def test():
    flask.flash("Testing mail sending !")

    mail_functions.send_mail(title="Hello world",
                             body="This is a test !",
                             recipients="sashakharoubi@gmail.com",
                             html=flask.render_template('mail.html', body="Hello World !")
                            )

    return flask.redirect('/')

@app.route("/")
def home():
    return flask.render_template("home.html")

@socketio.on('message')
def handleMessage(data):
    
    send(data)
    

@app.route("/messages")
def messages():

    all_users = models.User.query.filter_by(boolean=True)
    return flask.render_template("messages.html", all_users = all_users )

@app.route('/message', methods=['POST'])
def message():

    try:

        username = request.form.get('username')
        message = request.form.get('message')
        print(username)

        # new_message = Message(username=username1, message=message1)
        # db.session.add(new_message)
        # db.session.commit()

        pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message': message, 'time_stamp': strftime('%b-%d %I:%M%p', localtime())})

        return jsonify({'result' : 'success'})
    
    except:

        return jsonify({'result' : 'failure'})



@app.route("/sign-up", methods=["GET","POST"])
def signup():
    form = forms.SignUpForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            mail     = form.mail.data

            new_user = models.User(name = username, password = password, mail=mail)
            db.session.add(new_user)
            db.session.commit()
            mail_functions.send_mail(title="Welcome" +" "+ new_user.name ,
                            body="This is a test !",
                            recipients=new_user.mail,
                            html=flask.render_template('mail.html', body="Welcome to Hover Messaging, your new account"
                                                                        "is set up! You're good to go. You can now"
                                                                        "sign in into your account and start messaging ! "
                                                                        "Enjoy !")
                            )
            return flask.redirect('/sign-in')

        else:
            flask.flash("You haven't fill up the forms properly ! Please try again", "danger")

    
    
    return flask.render_template("signup.html", form=form)

#Route to display a list of the users registered

@app.route("/users")
def users_list():
    users = models.User.query.all()
    return flask.render_template("users_list.html", users=users)


#Route for profile

@app.route("/users/<int:user_id>")
def profile_page(user_id):
    user = models.User.query.get(user_id)
    return flask.render_template("user_page.html", user=user)



@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    
    form = forms.SignInForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
    
            # Retrieve the user that matches this username
            user = models.User.query.filter_by(name=username).first()
            print(user.boolean)

            # Check the provided password against the user's one
            if user is not None and user.password == password:
                flask_login.login_user(user)
                flask.flash(f"{user.name} logged in successfully !", "success")
                idn = user.id
                user.boolean = True
                db.session.commit()
                print(user.boolean)
                return flask.render_template('user_page.html', user=user)
            else:
                flask.flash("Something went wrong.", "danger") # Put the message into the flashed messages
                # To retrieve those messages: flask.get_flashed_messages()

    return flask.render_template("signin.html", form=form)

@app.route("/sign-out", methods=["GET"])
def signout():
    
    all_users = models.User.query.all()
    
    for user in all_users:
        if user.boolean == True:
            user.boolean = False
            print(user.boolean)
            db.session.commit() 
            print('OK')
            flask_login.logout_user()
            flask.flash("You successfully logout !", "danger")
            return flask.redirect('/sign-in')
        else:
            pass


























