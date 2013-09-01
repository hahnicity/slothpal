"""
slothpal.constants
~~~~~~~~~~~~~~~~~~
"""
## URL Endpoints ##
IDENTITY_ENDPOINT = "/v1/identity/openidconnect/tokenservice"
OAUTH2_ENDPOINT = "/v1/oauth2/token"
USER_INFO_ENDPOINT = "/v1/identity/openidconnect/userinfo/?schema=openid"

## Grant Types ##
AUTH_CODE = "authorization_code"
CLIENT_CRED = "client_credentials"
