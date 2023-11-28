from flask import render_template, request, url_for, redirect
from app.admin import bp
from app.extensions import db
from app.models.display_object import DisplayObject,DisplayObjectType


@bp.route("/", methods=("get"))
def index():
    display_objects = DisplayObject.query.all()
    return render_template('admin/index.html', list=display_objects)

@bp.route("/new", methods=("get", "post"))
def new():
    if request.method == "POST":
        result = DisplayObject(
            link= request.form["link"],
            display_name = request.form["display_name"],
            is_active = True,
            display_type = DisplayObjectType.LINK
        )
        db.session.add(result)
        db.session.commit()
        
        return render_template("admin/new.html", result=result)
    return render_template('admin/new.html')