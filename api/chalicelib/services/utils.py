from functools import wraps

from chalice import BadRequestError


def verify_integer_input(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if list(kwargs.values())[0].isdigit():
            return f(*args, **kwargs)
        else:
            raise BadRequestError("Integer Input Required")

    return decorated
