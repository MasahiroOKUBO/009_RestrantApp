
import httplib2
import json
import random
import string
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from sqlalchemy import asc
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
from flask import make_response

from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import Base
from RestaurantApp.utility import engine
from RestaurantApp.utility import db_session
from RestaurantApp.utility import CLIENT_ID
from RestaurantApp import app

def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    db_session.add(newUser)
    db_session.commit()
    user = db_session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = db_session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None





@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    del login_session['facebook_id']
    del login_session['access_token']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['state']
    return "you have been logged out"
