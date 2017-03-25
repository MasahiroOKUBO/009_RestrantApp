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




@app.route('/gdisconnect')
def gdisconnect():
    if not 'session' in request.cookies:
        print 'login_session is maybe None'
        response = make_response(json.dumps('Session does not exists in Cookie.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    if not login_session.has_key('access_token'):
        print 'login_session does not have access_token'
        response = make_response(json.dumps('login_session does not have access_token.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print login_session.keys()
    access_token = login_session['access_token']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Access Token is None'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # print login_session['credentials'].access_token
    print 'In gdisconnect access token is %s', login_session['access_token']
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['credentials']
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['state']
        del login_session['user_id']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
