from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def EditMenu(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    edited_menu = db_session.query(Menu).filter_by(id=menu_id).one()
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        if request.form['name']:
            edited_menu.name = request.form['name']
        if request.form['description']:
            edited_menu.description = request.form['description']
        if request.form['price']:
            edited_menu.price = request.form['price']
        if request.form['course']:
            edited_menu.course = request.form['course']
        db_session.add(edited_menu)
        db_session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('ShowRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template('form_edit_menu.html', restaurant_id=restaurant_id, menu_id=menu_id, item=edited_menu)
