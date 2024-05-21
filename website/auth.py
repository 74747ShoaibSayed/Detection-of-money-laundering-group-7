from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])#decorator defines route for hand login req qt url
def login():#view fun associate to login
    if request.method == 'POST':#if incoming req is post
        email = request.form.get('email')#This line extract email password submimitted via login from user flask
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()#queries databse for user with provided email id
        if user:
            if user.password == password:#checks password provided by user in form  matches with pass with form
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)#
                return redirect(url_for('views.home'))#after succesful login user is redirect to the homepage
            else:
                flash('Incorrect password, try again.', category='error')#wrong credentials or email not found in database
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')#decorator logout route
@login_required
def logout():#defining logout fun
    logout_user()#logout current user
    return redirect(url_for('auth.login'))#after logout this line redirect user to the login page


@auth.route('/sign-up', methods=['GET', 'POST'])#rout for sign-up
def sign_up():#Responsible for handling sign_up fun
    if request.method == 'POST':#if request method is post then
        email = request.form.get('email')#These lines retrieve form data submitted via POST request.
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()#it checks user already exist in database or not
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:#If all conditions pass, a new user is created, added to the database, and logged in. A success message is flashed, and the user is redirected to the home page.
            new_user = User(email=email, first_name=first_name, password=
                password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
#If the request method is not POST (i.e., it's a GET request), or if there were errors in the form submission, the sign-up form is rendered using the sign_up.html template, with the current user passed to the template for any necessary context.




