from flask import render_template
from flask import session as login_session
from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu
from RestaurantApp.utility import db_session
from RestaurantApp import app


def GetUserInfo(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def ShowRestaurant(restaurant_id):
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    creator = GetUserInfo(restaurant.user_id)
    menus = db_session.query(Menu).filter_by(restaurant_id=restaurant_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('page_restaurant_public.html',
                               items=menus,
                               restaurant=restaurant,
                               creator=creator)
    else:
        return render_template('page_restaurant_loginuser.html',
                               items=menus,
                               restaurant=restaurant,
                               creator=creator)
