from .routes import Taskly as Taskly_routes

from .auth import auth_routes
from .dashboard import dashboard_routes

Taskly_routes.register_blueprint(auth_routes, url_prefix='/auth')
Taskly_routes.register_blueprint(dashboard_routes, url_prefix='/dashboard')
