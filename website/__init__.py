from flask import Flask#starting flask application
from flask_sqlalchemy import SQLAlchemy#popular ORM library for working with database
from os import path#provides function for working with file path
from flask_login import LoginManager

db = SQLAlchemy()#acts as an interface to interact with database
DB_NAME = "database.db"


def create_app():#for creating flask appln
    app = Flask(__name__)#initializes flask app object
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'#sets seprate key for session security
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Manish%407733@localhost:3306/weatheria'#connct database uri with mysql database
    db.init_app(app)#db is instance of sqlalchemy
                    #this line binds sqlalchemy with flask app

    from .views import views#imports views blueprint from views.py
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')#register views blueprint with Flask appln
    app.register_blueprint(auth, url_prefix='/')
    #blueprint is a way to organize related routes

    from .models import User, Note#this import user and note model from import.py
    
    with app.app_context():#create database tables
        db.create_all()#crete all tables defined by models.

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader#It tolds flask-login how to load a user id
    def load_user(id):#fun takes user id as an argument
        return User.query.get(int(id))#

    return app


def create_database(app):#database create krta and takes app instance as an argument
    if not path.exists('website/' + DB_NAME):#it checks database path DB.NAME is name of database file
        db.create_all(app=app)
        print('Created Database!')
