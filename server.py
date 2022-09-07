from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined
import requests
import random


random_number = random.randint(1, 100)
value = 200
url = f"https://jservice.io//api/clues?value={value}"
response = requests.get(url)
print(response.json()[random_number]["question"])
print(response.json()[random_number]["answer"])
print(response.json()[random_number]["value"])


app = Flask(__name__)


@app.route("/")
def homepage():

    return render_template("trivia.html")


@app.route("/question")
def question():

    points = request.args.get("value")
    print("**********************")
    print(points)

    return render_template("trivia.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
