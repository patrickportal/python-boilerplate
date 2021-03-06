"""Return an initialized Flask application with the API."""
from flask import Flask

from mywebapp.api.api import create_api
from mywebapp.api.public_routes import heartbeat


def create_app() -> Flask:
    """Initialize a Flask app."""
    app = Flask(__name__)

    # Note: heartbeat is exposed without authentication
    app.register_blueprint(heartbeat.blueprint)

    api = create_api()
    app.register_blueprint(api)

    return app
