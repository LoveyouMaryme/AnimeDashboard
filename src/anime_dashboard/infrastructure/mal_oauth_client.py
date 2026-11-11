from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.infrastructure.oauth_token import OAuthTokens


class MALOAuthClient(OAuthClient):
    """"""

    """"""
    authorization_endpoint = "https://myanimelist.net/v1/oauth2/authorize"
    token_endpoint = "https://myanimelist.net/v1/oauth2/token"

    def __init__(
        self, redirect_uri: str, client_id: str, scope: str, client_secret: str
    ):
        self.redirect_uri = redirect_uri
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope

    def refresh(self, refresh_token: str) -> OAuthTokens: ...
