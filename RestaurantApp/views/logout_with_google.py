import httplib2
import json
from flask import request
from flask import session as login_session
from flask import make_response
from RestaurantApp import app


@app.route('/gdisconnect')
def LogoutWithGoogle():
    print 'request.cookies : %s' % request.cookies
    if 'session' not in request.cookies:
        print 'login_session is maybe None'
        response = make_response(json.dumps('Session does not exists in Cookie.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'login_session.keys : %s' % login_session.keys()
    if 'access_token' not in login_session.keys():
        print 'login_session does not have access_token'
        response = make_response(json.dumps('login_session does not have access_token.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session['access_token']
    print 'access_token : %s' % login_session['access_token']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Access Token is None'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    '''
    ================
       delete access_token
    ================
    '''
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result : %s' % result
    '''
    ================
       delete login_session
    ================
    '''
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
