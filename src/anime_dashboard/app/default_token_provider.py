from datetime import datetime

from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.app.token_provider import TokenProvider
from anime_dashboard.infrastructure.token_storage import TokenStorage


class DefaultTokenProvider(TokenProvider):
    """"""

    def __init__(self, auth: OAuthClient, storage: TokenStorage):
        self.auth = auth
        self.storage = storage

    def get_access_token(self) -> str:
        storage_info = self.storage.load()
        expiration_date = storage_info.expires_at
        access_token = storage_info.access_token
        refresh_token = storage_info.refresh_token

        if expiration_date > datetime.now():
            return access_token
        else:
            self.auth.refresh(refresh_token)
