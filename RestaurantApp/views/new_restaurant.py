from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
from RestaurantApp.models import Restaurant
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def NewRestaurant():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        new_restaurant = Restaurant(name=request.form['name'],
                                    user_id=login_session['user_id'])
        db_session.add(new_restaurant)
        db_session.commit()
        flash('New Restaurant %s Successfully Created' % new_restaurant.name)
        return redirect(url_for('ShowTop'))
    else:
        return render_template('form_new_restaurant.html')
