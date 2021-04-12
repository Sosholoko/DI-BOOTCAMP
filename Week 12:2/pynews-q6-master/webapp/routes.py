import flask

from . import app       # . is webapp/
from . import forms, news_functions, models, db
import flask_login

@app.route("/")
def home():
    return flask.render_template("base.html")

## Create a route:
# Form with one single field "query"
# Use the form data to display some articles about the query

# 1) Create the form        v
# 2) Create the route
# 3) Create the template that displays the form
# 4) Create the template that displays the articles

@app.route("/article/query/<query>")
def query_article(query):
    articles = news_functions.get_news(query)
    return flask.render_template("articles.html", articles=articles)

@app.route("/search-article", methods=["GET", "POST"])
def search_article():
    form = forms.QueryForm()

    # case 1: Post request --> The user is sending data
    if flask.request.method == "POST":
        if form.validate_on_submit(): # Check all the validators
            url = flask.url_for("query_article", query=form.query.data)
            # url --> /article/query/rick
            return flask.redirect(url)


    # case 2: Get request --> the user just wants to see the page
    return flask.render_template("search_article.html", form=form)

# Sign up page

# Create a page that displays a sign up form (username & password) and when it gets data from a user
# just print "Rick is signing up with password chocolate"

# The password needs to contain 6 to 12 characters
@app.route("/sign-up", methods=["GET","POST"])
def signup():
    form = forms.SignUpForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            new_user = models.User(name = username, password = password )
            db.session.add(new_user)
            db.session.commit()
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

            # Check the provided password against the user's one
            if user is not None and user.password == password:
                flask_login.login_user(user)
                flask.flash(f"{user.name} logged in successfully !", "success")
                idn = user.id
                return flask.render_template('user_page.html', user=user)
            else:
                flask.flash("Something went wrong.", "danger") # Put the message into the flashed messages
                # To retrieve those messages: flask.get_flashed_messages()

    return flask.render_template("signin.html", form=form)

@app.route("/sign-out")
def signout():
    flask_login.logout_user()
    return flask.redirect('/sign-in')



















# @app.route("/signin", methods=["GET", "POST"])
# def sign_in():
#     form = forms.SignInForm()

#     if flask.request.method == "POST":
#         if form.validate_on_submit():
#             username = form.username.data
#             password = form.password.data

#             user = models.User.query.filter_by(name = username)

#             if user is not None and user.password == password:
#                 flask_login.login_user(user)
#                 flask.flash("{user.name} logged in succesfully", "success")
#             else:
#                 flask.flash("Something went wrong", "danger")
    
#     return flask.render_template("signin.html", form = form)

    
# @app.route("/signout")
# def signout():
#     flask_login.logout_user(user)















