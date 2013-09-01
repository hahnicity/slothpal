"""
slothpal.user
~~~~~~~~~~~~~
"""
from requests import get

from slothpal import constants
from slothpal.headers import get_headers_with_bearer


def request_user_info(endpoint, token):
    """
    Make a request for user information
    """
    return get(
        "".join([endpoint, constants.USER_INFO_ENDPOINT]),
        headers=get_headers_with_bearer(token)
    ).json()
