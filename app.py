from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "dasodjasoadsasdsdadas"

@app.route("/lastshared")
def index():
    flash("AMO A BIANCA")
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    flash(f"Hi {str(request.form['name_input'])} kdoasadad.")
    return render_template("index.html")