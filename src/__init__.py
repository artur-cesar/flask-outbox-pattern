import os

from flask import Flask
from sqlalchemy import text

from src.controllers.hello_controller import hello_bp
from src.controllers.order_controller import order_bp
from src.extensions import db, migrate


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "templates"
        ),
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            print("Database connection OK!")
        except Exception as e:
            print(f"Database connection ERROR: {e}")

    app.register_blueprint(order_bp)
    app.register_blueprint(hello_bp)

    return app
