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


@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def NewMenu(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        # return "<script>function myFunction() {alert('You are not authorized to add menu items to this restaurant. Please create your own restaurant in order to add items.');}</script><body onload='myFunction()''>"
        render_template('alert.html')
    if request.method == 'POST':
        newItem = Menu(name=request.form['name'],
                       description=request.form['description'],
                       price=request.form['price'],
                       course=request.form['course'],
                       restaurant_id=restaurant_id,
                       user_id=restaurant.user_id)
        db_session.add(newItem)
        db_session.commit()
        flash('New Menu %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('ShowMenu', restaurant_id=restaurant_id))
    else:
        return render_template('form_new_menu.html', restaurant_id=restaurant_id)
