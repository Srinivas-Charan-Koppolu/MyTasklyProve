from flask import Blueprint

modules = Blueprint('modules', __name__)

from .auth import auth_routes
from .dashboard import dashboard_routes

modules.register_blueprint(auth_routes, url_prefix='/auth')
modules.register_blueprint(dashboard_routes, url_prefix='/dashboard')

