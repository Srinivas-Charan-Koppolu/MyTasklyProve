from flask import Blueprint
from . import views

verify = Blueprint("verify", __name__, template_folder="./templates", static_folder="./static")


@verify.route('/')
def index():
    return views.verify()