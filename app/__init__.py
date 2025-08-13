import os
from flask import Flask


def create_app():
    """Application factory for the Flask app."""
    template_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
    static_dir = os.path.join(os.path.dirname(__file__), "..", "static")

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object("app.config.Config")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
