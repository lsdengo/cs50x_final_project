from cs50 import SQL
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

db = SQL("sqlite:///cars.db")


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/trivia")
def trivia():
    return render_template("trivia.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/search_car")
def search_car():
    query = request.args.get("q")
    if query:
        cars = db.execute(
            "SELECT * FROM cars WHERE manufacturer LIKE ? COLLATE NOCASE", "%" + query + "%"
        )
    else:
        cars = []
    return jsonify(cars)


@app.route("/car/<int:car_id>")
def car_detail(car_id):
    car = db.execute("SELECT * FROM cars WHERE id = ?", car_id)
    if not car:
        return "Car not found", 404
    return render_template("search_car.html", car=car[0])


@app.route("/about")
def about():
    return render_template("about.html")
