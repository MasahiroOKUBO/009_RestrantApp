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


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def NewRestaurant():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'],
                                   user_id=login_session['user_id'])
        db_session.add(newRestaurant)
        flash('New Restaurant %s Successfully Created' % newRestaurant.name)
        db_session.commit()
        return redirect(url_for('ShowTop'))
    else:
        return render_template('form_new_restaurant.html')
