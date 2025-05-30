from flask import Blueprint, render_template

hello_bp = Blueprint("hello", __name__)


@hello_bp.route("/")
def hello():
    return render_template(
        "index.html",
        title="Página HTML5",
        heading="Bem-vindo!",
        message="Isso é HTML5 com Bootstrap.",
    )
