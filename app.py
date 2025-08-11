from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "This is Jayant Bhati projecct"

@app.route("/phone")
def lwphone():
	return "667788871"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
