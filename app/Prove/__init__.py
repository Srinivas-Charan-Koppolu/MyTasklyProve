from .routes import Prove as Prove_routes


from .verify import verify_routes

Prove_routes.register_blueprint(verify_routes, url_prefix="/verify")
