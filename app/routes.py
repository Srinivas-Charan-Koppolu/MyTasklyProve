from flask import Blueprint
from . import views

main = Blueprint('main', __name__, template_folder='./templates', static_folder='./static')

@main.route('/')
def index():
    return views.index()

@main.route('/about')
def about():
    return views.about()

@main.route('/seeUsers')
def see_users():
    return views.see_users()
