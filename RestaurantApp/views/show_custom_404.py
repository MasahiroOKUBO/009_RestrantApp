from flask import render_template
from RestaurantApp import app

@app.errorhandler(404)
def ShowCustom404(e):
    return render_template('page_custom_404.html'), 404


