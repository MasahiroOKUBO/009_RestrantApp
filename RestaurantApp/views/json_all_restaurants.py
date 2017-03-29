from flask import jsonify
from RestaurantApp.models import Restaurant
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/JSON/restaurants')
def JsonAllRestaurants():
    restaurants = db_session.query(Restaurant).all()
    return jsonify(restaurants=[r.serialize for r in restaurants])
