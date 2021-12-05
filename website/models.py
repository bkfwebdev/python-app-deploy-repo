from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150),unique = True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.string(150))

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


