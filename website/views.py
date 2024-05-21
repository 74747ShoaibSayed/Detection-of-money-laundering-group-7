from flask import Blueprint, render_template, request, flash, jsonify
#Blueprints in Flask are a way to organize a group of related views, templates, and static files.
#This function in Flask is used to render HTML templates. It takes the name of the template as an argument and optionally any variables you want to pass to the template.
#The request object in Flask allows you to access incoming request data, such as form data, files, cookies, and headers. It provides attributes and methods to access this data.
#Flask provides the flash function to display one-time messages to the user. These messages are typically used for feedback or notifications, such as success messages, error messages, or warnings.
from flask_login import login_required, current_user
#login-req--->route req for loggin user
#current user-->access for currently login user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])#for homepage
@login_required#logged-into access user
def home():#handles post request ,if submitted note is valid adding it to database
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:#if len is less than shows error message less than one
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note(): #for deleting a note
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
