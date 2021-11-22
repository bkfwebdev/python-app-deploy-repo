from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<h1>Login Page</h1>"

@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('/register')
def register():
    return "<h1>Register New U ser</h1>"
