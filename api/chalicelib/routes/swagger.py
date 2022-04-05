import json
import os

from chalice import Blueprint, Response
from jinja2 import Template

from chalicelib.cors import get_cors_config

swagger_routes = Blueprint(__name__)


@swagger_routes.route("/swagger_model.json", methods=["GET"], cors=get_cors_config())
def swagger_model_json_get():
    with open("chalicelib/public/swagger_model.json", "r") as f:
        model = json.load(f)
    model["basePath"] = f"/{os.getenv('API_STAGE')}"
    model["schemes"] = [os.getenv("API_SCHEME")]
    return model


@swagger_routes.route("/", methods=["GET"], cors=get_cors_config())
def swagger_model_get() -> Response:
    with open("chalicelib/public/swagger.html", "r") as f:
        html = f.read()
    template = Template(html)
    api_url = (
        f"{os.getenv('API_SCHEME')}://{os.getenv('API_URL')}/{os.getenv('API_STAGE')}"
        if os.getenv("API_STAGE")
        else f"{os.getenv('API_SCHEME')}://{os.getenv('API_URL')}"
    )
    return Response(body=template.render({"api_url": api_url}), status_code=200, headers={"Content-Type": "text/html"})
