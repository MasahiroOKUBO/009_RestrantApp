from flask import redirect, url_for, flash
from flask import session as login_session
from logout_with_google import LogoutWithGoogle
from logout_with_facebook import LogoutWithFacebook
from RestaurantApp import app


@app.route('/disconnect')
def Logout():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            LogoutWithGoogle()
        if login_session['provider'] == 'facebook':
            LogoutWithFacebook()
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('ShowTop'))
    else:
        flash("You were not logged in")
        return redirect(url_for('ShowTop'))
