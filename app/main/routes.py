from flask import render_template
from app.main import bp
from app.models.display_object import DisplayObject


@bp.route("/")
def index():
    display_objects = DisplayObject.query.all()
    return render_template('main/index.html', list=display_objects)

@bp.route("/login")
def login():
    return render_template('main/login.html')