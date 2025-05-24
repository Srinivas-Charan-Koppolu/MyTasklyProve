from flask import Blueprint
from . import views

Admin = Blueprint('Admin', __name__, template_folder="./templates", static_folder="./static")

@Admin.route('/')
def index():
    return views.adminPanel()