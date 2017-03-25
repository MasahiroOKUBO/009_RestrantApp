from RestaurantApp.models import User
from setup_database import db_session


def CreateUser(login_session):
    print "==================="
    print login_session['picture']
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])

    db_session.add(newUser)
    db_session.commit()
    user = db_session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def GetUserInfo(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


def GetUserID(email):
    try:
        user = db_session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None
