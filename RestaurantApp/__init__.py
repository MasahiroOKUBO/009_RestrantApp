from flask import Flask

app = Flask(__name__)

from views import ShowTop
from views import ShowRestaurant

from views import Login
from views import LoginWithGoogle
from views import LoginWithFacebook

from views import Logout
from views import LogoutWithGoogle
from views import LogoutWithFacebook

from views import NewRestaurant
from views import EditRestaurant
from views import DeleteRestaurant

from views import NewMenu
from views import EditMenu
from views import DeleteMenu

from views import JsonAllRestaurants
from views import JsonAllMenus
from views import JsonOneMenu

from views import ShowCustom404
