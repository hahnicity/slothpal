"""
slothpal.exceptions
~~~~~~~~~~~~~~~~~~~
"""


class StatusCodeError(Exception):
    def __init__(self, response):
        msg = (
            "You received a non-200 status code: <{} code> because {}."
            " Your response was {}".format(
                response.status_code, response.reason, response.content
            )
        )
        super(StatusCodeError, self).__init__(msg)
