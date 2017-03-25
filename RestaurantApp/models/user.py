from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from RestaurantApp.utility import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
