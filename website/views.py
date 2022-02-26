from flask import Blueprint, render_template, request, flash, jsonify 
from flask_login import login_required, current_user
from .models import Favorite
from . import db
import json
import requests

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
    url1 = "https://worldwide-restaurants.p.rapidapi.com/typeahead"
    url2 = "https://worldwide-restaurants.p.rapidapi.com/search"
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "worldwide-restaurants.p.rapidapi.com",
    'x-rapidapi-key': "5f44f5a205msh8e75909c98c9ec5p19b863jsnaab17199b013"
    }

    if request.method == 'POST':
         searchInput = request.form.get('searchInput')
         payload1 = f"q={searchInput}%20PA&language=en_US" 
         r1 = requests.request("POST", url1, data=payload1, headers=headers)
         data_json = json.loads(r1.text)
         location_id = data_json["results"]["data"][0]["result_object"]["location_id"]
         payload2 = f"language=en_US&limit=30&location_id={location_id}&currency=USD"
         r2 = requests.request("POST", url2, data=payload2, headers=headers)
         data_json = json.loads(r2.text)
         json_formatted_str = json.dumps(data_json, indent=2)
         print(json_formatted_str)

        #extract restauraunt data from r2 display data in view select favorites from view

    return render_template ('search.html', user = current_user)


@views.route('/manual-input', methods = ['GET', 'POST'])
def manual_imput():
    return render_template ('manual-restauraunt-form.html', user = current_user)


# add routes for delete-location, delete-preference, delete-favorite
