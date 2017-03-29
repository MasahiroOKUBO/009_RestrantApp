from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def NewMenu(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        new_menu = Menu(name=request.form['name'],
                        description=request.form['description'],
                        price=request.form['price'],
                        course=request.form['course'],
                        restaurant_id=restaurant_id,
                        user_id=restaurant.user_id)
        db_session.add(new_menu)
        db_session.commit()
        flash('New Menu %s Item Successfully Created' % (new_menu.name))
        return redirect(url_for('ShowRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template('form_new_menu.html', restaurant_id=restaurant_id)
