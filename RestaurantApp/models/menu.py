from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from user import User
from restaurant import Restaurant
from RestaurantApp.utility import Base


class Menu(Base):
    __tablename__ = 'menus'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
