from flask import render_template, Blueprint


users = Blueprint('users',__name__)

@users.route('/')
def index():
    return render_template("index.html")