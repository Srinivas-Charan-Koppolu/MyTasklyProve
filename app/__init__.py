from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)  # << add this

    from .models import User  # Import your models here to register them with SQLAlchemy

    from .routes import main
    from .Taskly import Taskly_routes
    from .Prove import Prove_routes

    # Register the blueprints
    app.register_blueprint(main)
    app.register_blueprint(Taskly_routes, url_prefix="/taskly")
    app.register_blueprint(Prove_routes, url_prefix="/prove")

    return app
