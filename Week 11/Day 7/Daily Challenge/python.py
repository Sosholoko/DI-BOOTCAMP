import flask


app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/<color>")
def color(color):
    return flask.render_template("color.html", color = color)




app.run(debug = True)