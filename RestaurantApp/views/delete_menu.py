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
from RestaurantApp import app



@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def DeleteMenu(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    itemToDelete = db_session.query(Menu).filter_by(id=menu_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete menu items to this restaurant. Please create your own restaurant in order to delete items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        db_session.delete(itemToDelete)
        db_session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('ShowMenu', restaurant_id=restaurant_id))
    else:
        return render_template('form_delete_menu.html', item=itemToDelete)