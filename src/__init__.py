from src.app_factory import create_app, db, migrate
from src.controllers.hello_controller import hello_bp
from src.controllers.order_controller import order_bp


def init_app(app):
    app.register_blueprint(hello_bp)
    app.register_blueprint(order_bp)
