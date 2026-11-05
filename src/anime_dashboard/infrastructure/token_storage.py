from typing import Protocol

from anime_dashboard.infrastructure.oauth_token import OAuthTokens


class TokenStorage(Protocol):
    def load(self) -> OAuthTokens | None: ...

    def save(self, tokens: OAuthTokens) -> None: ...
