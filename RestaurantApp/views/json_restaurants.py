
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



@app.route('/JSON/restaurants')
def JsonRestaurants():
    restaurants = db_session.query(Restaurant).all()
    return jsonify(restaurants=[r.serialize for r in restaurants])