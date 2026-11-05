from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.infrastructure.token_storage import TokenStorage


class DefaultTokenProvider:
    """"""

    def __init__(self, auth: OAuthClient, storage: TokenStorage):
        self.auth = auth
        self.storage = storage
