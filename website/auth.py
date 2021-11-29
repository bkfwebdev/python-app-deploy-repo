from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", testData = "this is a test string")

@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        email = request .form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than four characters.', category = 'error')
        elif len(firstName) < 2:
            flash('First name must be greater than two characters', category = 'error')
        elif password1 != password2:
            flash('Passwords do not match, please verify and re-type password', category = 'error')
        elif len(password1) < 7:
            flash('Passwords must be at least seven characters long', category = 'error')
        else:
            # add user to database
            flash('Account created!', category = 'success')




    return render_template("register.html")

