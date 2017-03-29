from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def DeleteMenu(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    item_to_delete = db_session.query(Menu).filter_by(id=menu_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        db_session.delete(item_to_delete)
        db_session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('ShowRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template('form_delete_menu.html', item=item_to_delete)
