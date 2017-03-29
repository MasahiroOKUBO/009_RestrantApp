from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from RestaurantApp.models import Restaurant
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def DeleteRestaurant(restaurant_id):
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if restaurant.user_id != login_session['user_id']:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        db_session.delete(restaurant)
        db_session.commit()
        flash('%s Successfully Deleted' % restaurant.name)
        return redirect(url_for('ShowTop', restaurant_id=restaurant_id))
    else:
        return render_template('form_delete_restaurant.html', restaurant=restaurant)
