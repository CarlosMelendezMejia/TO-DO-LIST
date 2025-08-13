import os


class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI",
        "mysql+pymysql://user:password@localhost/todo_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
