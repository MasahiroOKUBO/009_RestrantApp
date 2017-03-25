import httplib2
import json
import random
import string
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import make_response
from flask import session as login_session

from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import Base
from RestaurantApp.utility import engine
from RestaurantApp.utility import db_session
from RestaurantApp.utility import CLIENT_ID
from RestaurantApp import app


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def DeleteRestaurant(restaurant_id):
    restaurantToDelete = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if restaurantToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this restaurant. Please create your own restaurant in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        db_session.delete(restaurantToDelete)
        flash('%s Successfully Deleted' % restaurantToDelete.name)
        db_session.commit()
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('form_delete_restaurant.html', restaurant=restaurantToDelete)