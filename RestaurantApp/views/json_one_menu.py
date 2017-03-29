from flask import jsonify
from RestaurantApp.models import Menu
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/JSON/restaurants/<int:restaurant_id>/menu/<int:menu_id>')
def JsonOneMenu(menu_id):
    # def JsonOneMenu(restaurant_id, menu_id):
    menu = db_session.query(Menu).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=menu.serialize)
