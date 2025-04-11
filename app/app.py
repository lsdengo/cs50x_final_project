from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/trivia")
def trivia():
    return render_template("trivia.html")


@app.route("/about")
def about():
    return render_template("about.html")
