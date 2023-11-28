from enum import Enum, auto
from app.extensions import db


class DisplayObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(150))
    display_name = db.Column(db.String(150))
    thumbnail = db.Column(db.String(150))
    is_active = db.Column(db.Boolean)
    order = db.Column(db.Integer)
    display_type = db.Column(db.Integer)
    owner = db.Column(db.Integer)

class DisplayObjectType(Enum):
    LINK = auto()
    DIVIDER = auto()