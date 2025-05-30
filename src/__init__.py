from flask import Flask
from src.controllers.hello_controller import hello_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)

    return app
