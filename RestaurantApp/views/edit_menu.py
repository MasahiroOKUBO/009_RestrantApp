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


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def EditMenu(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = db_session.query(Menu).filter_by(id=menu_id).one()
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit menu items to this restaurant. Please create your own restaurant in order to edit items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        db_session.add(editedItem)
        db_session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('ShowMenu', restaurant_id=restaurant_id))
    else:
        return render_template('form_edit_menu.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)