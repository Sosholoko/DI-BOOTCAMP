import flask, flask_login

from . import main_blueprint, db       # . is webmain_blueprint/
from . import forms, news_functions, models, mail_functions
import flask_mail

@main_blueprint.route("/")
def home():
    return "Hello world !"

## Create a route:
# Form with one single field "query"
# Use the form data to display some articles about the query

# 1) Create the form        v
# 2) Create the route
# 3) Create the template that displays the form
# 4) Create the template that displays the articles

@main_blueprint.route("/article/query/<query>")
def query_article(query):
    articles = news_functions.get_news(query)
    return flask.render_template("articles.html", articles=articles)

@main_blueprint.route("/search-article", methods=["GET", "POST"])
def search_article():
    form = forms.QueryForm()

    # case 1: Post request --> The user is sending data
    if flask.request.method == "POST":
        if form.validate_on_submit(): # Check all the validators
            url = flask.url_for("main.query_article", query=form.query.data)
            # url --> /article/query/rick
            return flask.redirect(url)


    # case 2: Get request --> the user just wants to see the page
    return flask.render_template("search_article.html", form=form)


# Create a route that displays a list of all the registered users
@main_blueprint.route("/users")
def users_list():
    # Retrieve users
    users = models.User.query.all()            # Return a list of users
    # users = [<User 1>, <User 2>]
    # my_user = users[0]
    # print(my_user.name)
    # print(my_user.password)


    # Create users_list.html
    return flask.render_template("users_list.html", users=users)


# Route: profile page



@main_blueprint.route('/quotes')
def quotes_list():
    # Retrieve the quotes
    quotes = models.Quote.query.all()

    # display them on a temlate
    return flask.render_template("quotes.html", quotes=quotes)

@main_blueprint.route("/books")
def books_list():
    books = models.Book.query.all()

    return flask.render_template("books.html", books=books)

# Step 1: Displaying the favourite quote on the user page
# Step 2: (Because quote<->user is a one to one, one quote can be linked to only one user)
#       --> In quotes_list, display only the quotes that aren't the fav quote of a user
# Step 3: Creating a route fav_quote(quote_id) --> Sets the quote as the fav quote of the logged in
#        user
# Step 4: In the quotes_list: Add a button next to each quote (if the user is authenticated) to make
#        the quote his fav quote

@main_blueprint.route("/fav-quote/<int:quote_id>")
def fav_quote(quote_id):
    if flask_login.current_user.is_authenticated: # The user is logged in
        # Retrieve the quote
        quote = models.Quote.query.get(quote_id)

        # Set this quote as the current user's fav one
        flask_login.current_user.fav_quote = quote

        # Commit our changes
        db.session.commit()

    return flask.redirect("/quotes")


@main_blueprint.route("/fav_book/<int:book_id>")
def fav_book(book_id):
    if flask_login.current_user.is_authenticated: # The user is logged in
        book = models.Book.query.get(book_id) #book is an object of class Book

        if book not in flask_login.current_user.fav_books:
            flask_login.current_user.fav_books.main_blueprintend(book) # fav_books is a list of <Book> objects
            db.session.commit()

    else:
        flask.flash("You need to be logged in")
        return flask.redirect("/sign-in")

    return flask.redirect("/books")


@main_blueprint.route("/populate")
def populate():
    return "Protected"
    import requests
    url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"
    books = requests.get(url).json()

    for book in books:
        try:
            book_obj = models.Book(title=book["title"])
            db.session.add(book_obj)
        except:
            pass

    db.session.commit()

    return "OK"

@main_blueprint.route("/test")
def test():
    flask.flash("Testing Mail")
    mail_functions.send_mail(
"hello world",
"this is test",
"sashakharoubi@gmail.com",
html = flask.render_template("mail.html", body="Hello Sasha, Welcome to Hover Messaging"),
)

    return "Message Sent Succesfully"

