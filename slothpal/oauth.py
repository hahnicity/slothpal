"""
slothpal.oauth
~~~~~~~~~~~~~~
"""
from time import time

from requests import post

from slothpal import constants
from slothpal.exceptions import StatusCodeError
from slothpal.headers import get_oauth_headers


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
        return self.__token_response["expires_in"] + self.time_of_response

    def exchange_auth_code(self, code):
        """
        Exhange an authorization code for an access token for a client
        """
        response = post(
            "".join(
                [self.endpoint,
                 constants.IDENTITY_ENDPOINT,
                 "?grant_type={}".format(constants.AUTH_CODE),
                 "&code={}".format(code),
                 "&client_id={}".format(self.id),
                 "&client_secret={}".format(self.__secret)]
            ),
            headers=get_oauth_headers()
        )
        return response.json()

    # XXX This function will need to be re-thought
    def request_token(self):
        """
        Get an OAuth2 token from PayPal for our application
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
            self.__token_response = response.json()
