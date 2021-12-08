from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
 

class Preference(db.Model):
    id = db.column(db.Integer, primary_key=True)
    food_type = db.Column(db.String(150))
    user_id = db.Coulumn(db.Integer, db.ForeignKey('user.id'))

class Location(db.Model):
    id = db.column(db.Integer, primary_key=True)
    state = db.Column(db.String(150))
    city = db.Column(db.String(150))
    user_id = db.Coulumn(db.Integer, db.ForeignKey('user.id'))

class Favorite(db.Model):
    id = db.column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(150))
    restaurant_url = db.Column(db.String(150))
    user_id = db.Coulumn(db.Integer, db.ForeignKey('user.id'))


