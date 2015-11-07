from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
data_base = MongoClient()
mongo = data_base.tedhenat

app = Flask(__name__)
@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")
@app.route("/save", methods=["POST"])
def save():
	first_name = request.form["firstname"]
	last_name = request.form["lastname"]
	json_doc = {
		"first_name": first_name,
		"last_name":last_name
	}
	mongo.personi.insert(json_doc)

	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5050)