import httplib2
from flask import session as login_session
from RestaurantApp import app


@app.route('/fbdisconnect')
def LogoutWithFacebook():
    facebook_id = login_session['facebook_id']
    access_token = login_session['access_token']
    '''
    ================
       delete access_token
    ================
    '''
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    print "url : %s" % url
    print "result : %s" % result
    '''
    ================
       delete login_session
    ================
    '''
    del login_session['facebook_id']
    del login_session['access_token']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['state']

    return "you have been logged out"
