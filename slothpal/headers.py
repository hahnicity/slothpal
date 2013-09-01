"""
slothpal.headers
~~~~~~~~~~~~~~~~
"""


def get_headers_with_bearer(token):
    """
    Get necessary headers to make an identity call for user information
    """
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }


def get_oauth_headers():
    """
    Get request headers for the oauth token request
    """
    return {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
