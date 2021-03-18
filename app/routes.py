from app import app
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Morgana'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title = 'Home', user = user, posts = posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.values.get("user"), request.values.get("pass"), request.values.get("remember"))
    return render_template("login.html", title="Login")