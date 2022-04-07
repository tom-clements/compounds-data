from chalice import Blueprint, Response

from chalicelib.cors import get_cors_config
from chalicelib.services.compound.get_compound_from_id import get_compound_from_id
from chalicelib.services.compound.get_compound_ids import get_compound_ids
from chalicelib.services.compound.get_compound_image_from_id import (
    get_compound_image_from_id,
    get_compound_image_html_from_id,
)
from chalicelib.services.utils import verify_integer_input

compound_routes = Blueprint(__name__)


@compound_routes.route("/compound", methods=["GET"], cors=get_cors_config())
def compound_get() -> Response:
    return Response(body=get_compound_ids(), status_code=200)


@compound_routes.route("/compound/{compound_id}", methods=["GET"], cors=get_cors_config())
@verify_integer_input
def compound_from_id_get(compound_id: str) -> Response:
    compound = get_compound_from_id(int(compound_id))
    if compound:
        return Response(body=compound, status_code=200)
    else:
        return Response(body={"message": "Compound Not Found"}, status_code=404)


@compound_routes.route("/compound/{compound_id}/image.png", methods=["GET"], cors=get_cors_config())
@verify_integer_input
def compound_image_from_id_get(compound_id: str) -> Response:
    image = get_compound_image_from_id(int(compound_id))
    if image:
        return Response(body=image, status_code=200, headers={"Content-Type": "image/png"})
    else:
        return Response(body={"message": "Compound Not Found"}, status_code=404)


@compound_routes.route("/compound/{compound_id}/image.html", methods=["GET"], cors=get_cors_config())
@verify_integer_input
def compound_image_html_from_id_get(compound_id: str) -> Response:
    html = get_compound_image_html_from_id(int(compound_id))
    if html:
        return Response(body=html, status_code=200, headers={"Content-Type": "text/html"})
    else:
        return Response(body={"message": "Compound Not Found"}, status_code=404)
