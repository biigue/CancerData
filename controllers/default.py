from flask import render_template
from CancerData import app


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")