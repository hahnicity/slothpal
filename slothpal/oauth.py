"""
slothpal.oauth
~~~~~~~~~~~~~~
"""
from time import time

from requests import post

from slothpal import constants
from slothpal.exceptions import StatusCodeError
from slothpal.headers import get_oauth_headers


def get_expiry_time(response, time_of_response=time()):
    """
    Get the time a token will expire
    """
    return int(response["expires_in"]) + int(time_of_response)


class OAuth(object):
    def __init__(self, endpoint, id, secret):
        self.endpoint = endpoint
        self.id = id
        self.__secret = secret
        self.__token_response = dict()

    # XXX The existence of these properties should be reconsidered
    @property
    def scope(self):
        return self.__token_response["scope"]

    @property
    def token(self):
        return self.__token_response["access_token"]

    @property
    def expiry(self):
        return get_expiry_time(self.__token_response, self.time_of_response)

    def exchange_auth_code(self, code):
        """
        Exhange an authorization code for an access token for a client
        """
        response = self._perform_tokenservice_post(
            constants.AUTH_CODE, code=code
        )
        return response.json()

    def _perform_tokenservice_post(self, grant_type, **kwargs):
        """
        Make a post to the PayPal
        """
        return post(
            "".join([self.endpoint, constants.TOKENSERVICE_ENDPOINT]),
            data="&".join([
                "grant_type={}".format(constants.AUTH_CODE),
                "client_id={}".format(self.id),
                "client_secret={}".format(self.__secret)] +
                ["{}={}".format(key, value) for key, value in kwargs.iteritems()]),
            headers=get_oauth_headers()
        )

    # XXX This function will need to be re-thought
    def request_token(self):
        """
        Get an token from PayPal for our application
        """
        response = post(
            "".join([self.endpoint, constants.OAUTH2_ENDPOINT]),
            headers=get_oauth_headers(),
            data="grant_type={}".format(constants.CLIENT_CRED),
            auth=(self.id, self.__secret)
        )
        self.time_of_response = time()
        if response.status_code != 200:
            raise StatusCodeError(response)
        else:
            # XXX This cannot be stored
            self.__token_response = response.json()

    def use_refresh_token(self, refresh_token):
        """
        Get a token using a client's refresh request token
        """
        response = self._perform_tokenservice_post(
            constants.REFRESH_TOKEN, refresh_token=refresh_token
        )
        return response.json()
