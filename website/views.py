from flask import Blueprint, render_template, request, flash, jsonify 
from flask_login import login_required, current_user
from .models import Favorite
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        RestaurauntName = request.form.get('RestaurauntName')
        PhoneNumber = request.form.get('PhoneNumber')
        Website = request.form.get('Website')
        StreetAddress = request.form.get('StreetAddress')

        if len('RestaurauntName') < 1:
            flash('Data entered incorrectly!', category = 'error')
        else:
            new_favorite = Favorite(RestaurauntName = RestaurauntName, PhoneNumber = PhoneNumber, Website = Website, StreetAddress = StreetAddress, user_id = current_user.id)
            db.session.add(new_favorite)
            db.session.commit()
            flash('favorite added!', category = 'success')

    return render_template('home.html', user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})

@views.route('/search-request', methods = ['GET','POST'])
def search_request():
    return render_template ('search.html', user = current_user)


@views.route('/manual-input', methods = ['GET', 'POST'])
def manual_imput():
    return render_template ('manual-restauraunt-form.html', user = current_user)


# add routes for delete-location, delete-preference, delete-favorite
