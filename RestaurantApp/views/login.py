import random
import string
from flask import render_template
from flask import session as flask_session
from RestaurantApp.utility import GOOGLE_CLIENT_ID
from RestaurantApp.utility import FACEBOOK_APP_ID
from RestaurantApp import app


@app.route('/login')
def Login():
    # state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    state = ''
    for i in range(32):
        state += state.join(random.choice(string.ascii_uppercase + string.digits))
    flask_session['state'] = state
    print "print state " + state
    return render_template('page_login.html',
                           STATE=state,
                           CLIENT_ID=GOOGLE_CLIENT_ID,
                           APP_ID=FACEBOOK_APP_ID)
