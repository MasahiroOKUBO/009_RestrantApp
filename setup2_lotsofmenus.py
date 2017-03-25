from RestaurantApp.utility import db_session
from RestaurantApp.models import User
from RestaurantApp.models import Restaurant
from RestaurantApp.models import Menu

User1 = User(name="Robo Barista",
             email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')

Restaurant1 = Restaurant(user_id=1,
                         name="Urban Burger")

MenuItem1 = Menu(user_id=1,
                 name="French Fries",
                 description="with garlic and parmesan",
                 price="$2.99",
                 course="Appetizer",
                 restaurant=Restaurant1)

MenuItem2 = Menu(user_id=1,
                 name="Veggie Burger",
                 description="Juicy grilled veggie patty with tomato mayo and lettuce",
                 price="$7.50",
                 course="Entree",
                 restaurant=Restaurant1)

db_session.add(User1)
db_session.add(Restaurant1)
db_session.add(MenuItem1)
db_session.add(MenuItem2)
db_session.commit()

print "added menu items!"
