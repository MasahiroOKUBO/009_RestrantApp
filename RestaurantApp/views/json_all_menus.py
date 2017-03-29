from flask import jsonify
from RestaurantApp.models import Menu
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/JSON/restaurants/<int:restaurant_id>/menu/')
def JsonAllMenus(restaurant_id):
    menus = db_session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(Menus=[menu.serialize for menu in menus])
