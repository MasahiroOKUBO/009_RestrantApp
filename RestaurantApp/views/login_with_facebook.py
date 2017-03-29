import httplib2
import json
from flask import render_template, request, flash
from flask import session as login_session
from flask import make_response
from RestaurantApp.models import User
from RestaurantApp.utility import db_session
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


@app.route('/login_with_facebook', methods=['POST'])
def LoginWithFacebook():
    print request.args.get('state')
    print login_session['state']
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    '''
    ================
       read client_secret_facebook.json
    ================
    '''
    json_content = json.loads(open('client_secret_facebook.json', 'r').read())
    print "json_content : %s" % json_content
    app_id = json_content['web']['app_id']
    app_secret = json_content['web']['app_secret']
    access_token = request.data
    print "app_id : %s" % app_id
    print "app_secret : %s" % app_secret
    print "access_token : %s" % access_token
    '''
    ================
       get fb token
    ================
    '''
    url = 'https://graph.facebook.com/oauth/access_token' \
          '?grant_type=fb_exchange_token' \
          '&client_id=%s' \
          '&client_secret=%s' \
          '&fb_exchange_token=%s' % (app_id, app_secret, access_token)
    print "url : %s" % url
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    print "result : %s" % result
    data = json.loads(result)
    token = 'access_token=' + data['access_token']
    # token = result.split("&")[0]
    stored_token = token.split("=")[1]
    print "token : %s" % token
    print "stored_token : %s" % stored_token

    '''
    ================
       get fb user info
    ================
    '''
    url = 'https://graph.facebook.com/v2.8/me' \
          '?%s' \
          '&fields=name,id,email' % token
    print "url : %s" % url
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    json_content = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = json_content["name"]
    login_session['email'] = json_content["email"]
    login_session['facebook_id'] = json_content["id"]
    login_session['access_token'] = stored_token
    print "result : %s" % result
    print "json_content : %s" % json_content
    print "provider : %s" % login_session['provider']
    print "username : %s" % login_session['username']
    print "email : %s" % login_session['email']
    print "facebook_id : %s" % login_session['facebook_id']
    print "access_token : %s" % login_session['access_token']

    '''
    ================
       get fb user pic
    ================
    '''
    url = 'https://graph.facebook.com/v2.8/me/picture' \
          '?%s' \
          '&redirect=0' \
          '&height=200' \
          '&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    json_content = json.loads(result)
    picture_url = json_content["data"]["url"]
    login_session['picture'] = picture_url
    print "picture : %s" % login_session['picture']
    '''
    ================
       if email not registerd, create new user.
    ================
    '''
    user_id = getUserID(login_session['email'])
    print "user_id : %s" % user_id
    if not user_id:
        user_id = createUser(login_session)
        print "Create New User !"
    login_session['user_id'] = user_id

    '''
    ================
       render login confirm page
    ================
    '''
    print "login_session : %s" % login_session
    flash("Now logged in as %s" % login_session['username'])
    return render_template('page_login_confirm.html',
                           username=login_session['username'],
                           picture=login_session['picture'])
