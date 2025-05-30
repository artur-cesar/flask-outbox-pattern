import os

from flask import Flask

from src import create_app

app = create_app()

if __name__ == "__main__":
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=debug)
