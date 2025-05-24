from flask import Blueprint
from . import views
from config import Config

dashboard = Blueprint('dashboard', __name__, template_folder='./templates', static_folder='./static')


@dashboard.route('/')
def index():
    if not Config.ENABLE_DASHBOARD:
        return views.dashboard_disabled()
    return views.dashboard()

