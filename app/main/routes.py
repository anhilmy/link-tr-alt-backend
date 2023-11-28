from flask import render_template
from app.main import bp


@bp.route("/")
def index():
    return render_template('main/index.html')

@bp.route("/login")
def login():
    return render_template('main/login.html')