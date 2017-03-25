from flask import Flask

app = Flask(__name__)

from views import DeleteMenu
from views import DeleteRestaurant
from views import EditMenu
from views import EditRestaurant
from views import Login
from views import NewMenu
from views import NewRestaurant
from views import ShowMenu
from views import JsonRestaurants
from views import JsonRestaurantAllMenus
from views import JsonOneMenu
from views import gconnect
from views import fbconnect
from views import ShowTop
from views import gdisconnect
from views import fbdisconnect
from views import disconnect
