from flask import Blueprint, render_template, request, flash, jsonify 
from flask_login import login_required, current_user
from .models2 import Favorite
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        favorite = request.form.get('favorite')
        if len(favorite) < 1:
            flash('URL is too short', category = 'error')
        else:
            new_favorite = Favorite(data = favorite, user_id = current_user.id)
            db.session.add(new_favorite)
            db.session.commit()
            flash('URL added!', category = 'success')

    return render_template('home.html', user = current_user)

@views.route('/delete-favorite', methods = ['POST'])
def delete_favorite():
    favorite = json.loads(request.data)
    favoriteId = favorite['favoriteId']
    favorite = Favorite.query.get(favoriteId)
    if favorite:
        if favorite.user_id == current_user.id:
            db.session.delete(favorite)
            db.session.commit()
            return jsonify({})

@views.route('/search-request', methods = ['GET','POST'])
def search_request():
    return render_template ('search.html', user = current_user)


@views.route('/manual-input', methods = ['GET', 'POST'])
def manual_imput():
    return render_template ('manual-restauraunt-form.html', user = current_user)


# add routes for delete-location, delete-preference, delete-favorite
