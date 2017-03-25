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
from RestaurantApp.utility import GetUserID
from RestaurantApp.utility import GetUserInfo
from RestaurantApp import app


def GetUserInfo(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def ShowMenu(restaurant_id):
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    print restaurant
    print restaurant.user_id
    creator = GetUserInfo(restaurant.user_id)
    print creator
    menus = db_session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('page_restaurant_public.html',
                               items=menus,
                               restaurant=restaurant,
                               creator=creator)
    else:
        return render_template('page_restaurant_user.html',
                               items=menus,
                               restaurant=restaurant,
                               creator=creator)
