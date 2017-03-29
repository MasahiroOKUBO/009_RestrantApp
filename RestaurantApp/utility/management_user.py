from RestaurantApp.models import User
from setup_database import db_session


def CreateUser(login_session):
    new_user = User(name=login_session['username'],
                    email=login_session['email'],
                    picture=login_session['picture'])
    db_session.add(new_user)
    db_session.commit()
    user_obj = db_session.query(User).filter_by(email=login_session['email']).one()
    print "user_obj : %s" % user_obj
    return user_obj.id


def GetUserObj(user_id):
    user_obj = db_session.query(User).filter_by(id=user_id).one()
    return user_obj


def GetUserID(email):
    try:
        user_obj = db_session.query(User).filter_by(email=email).one()
        return user_obj.id
    except:
        return None
