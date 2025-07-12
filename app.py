from flask import Flask

app = Flask(__name__)


@app.route("/info")
def lwinfo():
	return "This is Jayant Bhati"

@app.route("/phone")
def lwphone():
	return "66771661551771"

app.run(host="0.0.0.0")