from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       email = request.form.get('email')
       password = request.form.get('password')
       user = User.query.filter_by(email=email).first()
       if user:
           if check_password_hash(user.password, password):
               flash('Logged in succesfully', category='success')
           else:
               flash('Login error, please verify login credentials',
                     category='error')
       else:
           flash('Email/User Does not exist.', category='error')
   return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        email = request .form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('This user already exist.', category = 'error')
            

        if len(email) < 4:
            flash('Email must be greater than four characters.', category = 'error')
        elif len(first_name) < 2:
            flash('First name must be greater than two characters', category = 'error')
        elif password1 != password2:
            flash('Passwords do not match, please verify and re-type password', category = 'error')
        elif len(password1) < 7:
            flash('Passwords must be at least seven characters long', category = 'error')
        else:
            # add user to database
            new_user = User(email = email, first_name = first_name,password = generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category = 'success')
            return redirect(url_for('views.home'))



    return render_template("register.html")

