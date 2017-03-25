
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import Base
from RestaurantApp.utility import engine
from RestaurantApp.utility import db_session
from RestaurantApp.utility import CLIENT_ID
from RestaurantApp import app

@app.route('/JSON/restaurants/<int:restaurant_id>/menu/')
def JsonRestaurantAllMenus(restaurant_id):
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = db_session.query(Menu).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(Menus=[i.serialize for i in items])