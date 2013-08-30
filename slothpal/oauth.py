"""
slothpal.oauth
~~~~~~~~~~~~~~
"""
from time import time

from requests import post

from slothpal.constants import GRANT_TYPE, OAUTH_ENDPOINT
from slothpal.exceptions import StatusCodeError


class OAuth(object):
    def __init__(self, endpoint, id, secret):
        self.endpoint = endpoint
        self.__id = id
        self.__secret = secret
        self.__token_response = dict()

    @property
    def token(self):
        return self.__token_response["access_token"]

    @property
    def expiry(self):
        return self.__token_response["expires_in"] + self.time_of_response

    def get_headers(self):
        """
        Get request headers for the oauth token request
        """
        return {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def request_token(self):
        """
        Get an OAuth2 token from PayPal
        """
        response = post(
            "".join([self.endpoint, OAUTH_ENDPOINT]),
            headers=self.get_headers(),
            data="grant_type={}".format(GRANT_TYPE),
            auth=(self.__id, self.__secret)
        )
        self.time_of_response = time()
        if response.status_code != 200:
            raise StatusCodeError(response)
        else:
            self.__token_response = response.json()
