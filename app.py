import os

from src import create_app, init_app

app = create_app()
init_app(app)

if __name__ == "__main__":
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=5000, debug=debug, use_reloader=debug)
