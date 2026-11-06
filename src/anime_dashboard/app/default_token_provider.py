from datetime import datetime, timezone

from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.app.token_provider import TokenProvider
from anime_dashboard.infrastructure.token_storage import TokenStorage


class DefaultTokenProvider(TokenProvider):
    """"""

    def __init__(self, auth: OAuthClient, storage: TokenStorage):
        self.auth = auth
        self.storage = storage

    def get_access_token(self) -> str:
        """
        Get access token in the storage if it is still valid,
        if not will recreate a new one

        return:
            access_token

        """
        if self.storage:
            storage_info = self.storage.load()

            expiration_date = storage_info.expires_at
            access_token = storage_info.access_token
            refresh_token = storage_info.refresh_token
        else:
            raise ValueError("Access token hasn't been initialized")

        if expiration_date > datetime.now(timezone.utc):
            return access_token
        else:
            new_oauth_token = self.auth.refresh(refresh_token)
            self.storage.save(new_oauth_token)
            new_access_token = new_oauth_token.access_token
            return new_access_token
