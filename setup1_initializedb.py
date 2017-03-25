from RestaurantApp.utility import Base
from RestaurantApp.utility import engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
