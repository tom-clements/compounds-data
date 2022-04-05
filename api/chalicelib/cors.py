from chalice import CORSConfig


# TODO: configure CORS to not all from all origins
def get_cors_config(allow_origin: str = "*") -> CORSConfig:
    return CORSConfig(
        allow_origin=allow_origin,
        allow_headers=["X-Special-Header"],
        max_age=600,
        expose_headers=["X-Special-Header"],
        allow_credentials=True,
    )
