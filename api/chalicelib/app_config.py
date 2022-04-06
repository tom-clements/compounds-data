import logging

from chalice import Chalice

from chalicelib.routes.compound import compound_routes
from chalicelib.routes.swagger import swagger_routes


def register_blueprints(app: Chalice):
    app.register_blueprint(compound_routes)
    app.register_blueprint(swagger_routes)


def set_log_level(app):
    app.log.setLevel(logging.INFO)


def setup_app() -> Chalice:
    chalice_app = Chalice(app_name="compounds-data", debug=False)
    set_log_level(chalice_app)
    register_blueprints(chalice_app)
    return chalice_app
