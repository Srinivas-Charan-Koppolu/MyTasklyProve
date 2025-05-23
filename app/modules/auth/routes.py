from flask import Blueprint
from . import views
from config import Config 

auth = Blueprint('auth', __name__, template_folder='./templates', static_folder='./static')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if not Config.ENABLE_AUTH:
        return views.auth_disabled_index()
    return views.register()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if not Config.ENABLE_AUTH:
        return views.auth_disabled_index()
    return views.login()

@auth.route('/logout')
def logout():
    return views.logout()
