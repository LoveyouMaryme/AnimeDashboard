from typing import Protocol

from anime_dashboard.infrastructure.oauth_token import OAuthTokens


class OAuthClient(Protocol):
    """"""

    def refresh(self, refresh_token: str) -> OAuthTokens: ...
