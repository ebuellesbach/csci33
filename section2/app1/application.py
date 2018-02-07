# GOAL: Like app0 but with any name in the URL

# imports
from flask import Flask, render_template

# start the app
app = Flask(__name__)

# add a default route to index
@app.route("/")
def index():
	return render_template("index.html")

# add a route to say hello to any name
@app.route("/<string:n>")
def hello():
	return render_template("hello.html", name=n)
