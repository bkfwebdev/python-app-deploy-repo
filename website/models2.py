from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    phone = db.Column(db.String(10000))
    website = db.Column(db.String(10000))
    address = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    favorites = db.relationship('Favorite')
 


