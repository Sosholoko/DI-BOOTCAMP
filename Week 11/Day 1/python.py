import flask
import random
import requests     # "Module not found" --> pip install requests
import datetime





#print(get_news('israel'))

#create a controller

app = flask.Flask(__name__)


url = "https://newsapi.org/v2/everything"
token = "5719809a4f814d0d9f8cb98e7a3d97de"

def get_news(query):
    params = {
        "apiKey": token,
        "q": "query",
        "from": "2021-03-01"
    }

    results = requests.get(url, params=params)
    return results.json()['articles']

#@app.route("/")
@app.route("/home")
def homepage():
    return "<html> <h1>Hello World !</h1><html>"

# def prettify_article(article):
#     return f"""
#         <div>
#             <p> {article['title']} </p>
#             <p> {article['description']} </p>
#             <small> {article['author']}</small>
#         </div> 
#     """

@app.route("/random")
def numpage():
    num = random.randint(1, 100)
    return f"<html> {num} </html>"

@app.route("/username/<name>")
def greeting(name):
    return flask.render_template("article.html", name=name)

@app.route("/legal/<age>")
def checkage(age):
    if int(age) < 18:
        return f"You're too young to buy alcoohol ! You're only {age} years old"
    else:
        return f"Alright you're {age} years old, enjoy !"

# @app.route("/news/<article>")
# def news(article):
#     articles = get_news(article)[:5]
#     html = "<html>\n"
#     for article in articles:
#         html += prettify_article(article)

#     html += "</html>"
#     return html

@app.route("/news/<topic>")
def news(topic):
    articles = get_news(topic)[:5]
    return flask.render_template("article2.html", articles=articles)

@app.route('/time')
def hour():
    #date = datetime.datetime.now()
    nowTime = datetime.datetime.now()
    return flask.render_template("hour.html", date = nowTime)






#run the app

app.run(debug = True)