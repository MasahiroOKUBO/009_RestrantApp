from sqlalchemy import asc
from flask import render_template
from flask import session as login_session
from RestaurantApp.models import Restaurant
from RestaurantApp.utility import db_session
from RestaurantApp import app


@app.route('/')
@app.route('/restaurant/')
def ShowTop():
    restaurants = db_session.query(Restaurant).order_by(asc(Restaurant.name))
    if 'username' not in login_session:
        return render_template('page_top_public.html', restaurants=restaurants)
    else:
        return render_template('page_top_loginuser.html', restaurants=restaurants)
