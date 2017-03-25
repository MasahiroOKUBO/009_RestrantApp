
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session

from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import Base
from RestaurantApp.utility import engine
from RestaurantApp.utility import db_session
from RestaurantApp.utility import CLIENT_ID
from RestaurantApp import app

@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def EditRestaurant(restaurant_id):
    editedRestaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedRestaurant.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this restaurant. Please create your own restaurant in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
            return redirect(url_for('ShowTop'))
    else:
        return render_template('form_edit_restaurant.html', restaurant=editedRestaurant)