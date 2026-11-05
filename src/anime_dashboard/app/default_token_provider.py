from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.app.token_provider import TokenProvider
from anime_dashboard.infrastructure.token_storage import TokenStorage


class DefaultTokenProvider(TokenProvider):
    """"""

    def __init__(self, auth: OAuthClient, storage: TokenStorage):
        self.auth = auth
        self.storage = storage

    def get_access_token(self) -> str:
        pass
