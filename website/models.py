from . import db#db is the obj of sqlA1chem
from flask_login import UserMixin#is a class
from sqlalchemy.sql import func



class Note(db.Model):#for storing notes in database
    id = db.Column(db.Integer, primary_key=True)#an integer field containing primary key
    data = db.Column(db.String(10000))#string field to contain note of string
    date = db.Column(db.DateTime(timezone=True), default=func.now())#gets automatic current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#foreign key interact with user table


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)#primary key
    email = db.Column(db.String(150), unique=True)#for storing email add
    password = db.Column(db.String(150))#for storing password
    first_name = db.Column(db.String(150))#for storing 1st name
    notes = db.relationship('Note')#relationship between user and note
