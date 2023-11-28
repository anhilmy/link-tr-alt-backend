from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
