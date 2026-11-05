from datetime import datetime, timezone

from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.infrastructure.oauth_token import OAuthTokens


class FakeOAuthClient(OAuthClient):
    def __init__(self, default_oauth_token: OAuthTokens, counter: int = 0):
        self.default_oauth_token = default_oauth_token
        self.counter = counter

    def refresh(self, refresh_token: str) -> OAuthTokens:
        if refresh_token == self.default_oauth_token.refresh_token:
            self.counter += 1

            new_token = OAuthTokens(
                f"new_access_token_{self.counter}",
                f"new_fresh_token_{self.counter}",
                datetime.now(timezone.utc),
            )

            self.default_oauth_token = new_token
            return new_token
        else:
            raise ValueError("Not the right refresh_token")
