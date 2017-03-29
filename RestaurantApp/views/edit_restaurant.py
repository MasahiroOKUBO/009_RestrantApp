from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from RestaurantApp.models import Restaurant
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def EditRestaurant(restaurant_id):
    edited_restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if edited_restaurant.user_id != login_session['user_id']:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        if request.form['name']:
            edited_restaurant.name = request.form['name']
            flash('Restaurant Successfully Edited %s' % edited_restaurant.name)
            return redirect(url_for('ShowTop'))
    else:
        return render_template('form_edit_restaurant.html', restaurant=edited_restaurant)
