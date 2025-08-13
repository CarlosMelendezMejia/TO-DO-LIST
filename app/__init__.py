import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Import models so they are registered with SQLAlchemy
from .models import User, Role, Permission  # noqa: F401


def create_app():
    """Application factory for the Flask app."""
    template_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
    static_dir = os.path.join(os.path.dirname(__file__), "..", "static")

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object("app.config.Config")
    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
