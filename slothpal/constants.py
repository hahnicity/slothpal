"""
slothpal.constants
~~~~~~~~~~~~~~~~~~
"""
## PayPal URLS
SANDBOX_ENDPOINT = "https://api.sandbox.paypal.com"
LIVE_ENDPOINT = "https://api.paypal.com"

## URL Endpoints ##
AUTHORIZE_ENDPOINT = "/webapps/auth/protocol/openidconnect/v1/authorize"
OAUTH2_ENDPOINT = "/v1/oauth2/token"
TOKENSERVICE_ENDPOINT = "/v1/identity/openidconnect/tokenservice"
USER_INFO_ENDPOINT = "/v1/identity/openidconnect/userinfo/?schema=openid"

## Grant Types ##
AUTH_CODE = "authorization_code"
CLIENT_CRED = "client_credentials"
REFRESH_CODE = "refresh_token"

## Response Types
CODE = "code"
