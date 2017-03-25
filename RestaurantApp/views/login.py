import random
import string


from flask import Flask, render_template
from flask import session as login_session

from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import Base
from RestaurantApp.utility import engine
from RestaurantApp.utility import db_session
from RestaurantApp.utility import CLIENT_ID
from RestaurantApp import app


@app.route('/login')
def Login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('page_login.html', STATE=state)
