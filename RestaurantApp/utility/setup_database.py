from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///RestaurantApp/data/restaurantapp.db')
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()
