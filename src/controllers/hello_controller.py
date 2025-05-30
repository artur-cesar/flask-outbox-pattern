from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def hello():
    return "Hello, World!!!"