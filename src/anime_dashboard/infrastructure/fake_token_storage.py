from anime_dashboard.infrastructure.oauth_token import OAuthTokens
from anime_dashboard.infrastructure.token_storage import TokenStorage


class FakeTokenStorage(TokenStorage):
    """
    Simulate a Token Storage for test purposes

    """

    def __init__(self, tokens: OAuthTokens | None = None):
        self.tokens = tokens

    def load(self) -> OAuthTokens | None:
        return self.tokens
