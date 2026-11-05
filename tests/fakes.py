from datetime import datetime, timezone

from anime_dashboard.app.oauth_client import OAuthClient
from anime_dashboard.infrastructure.oauth_token import OAuthTokens


class FakeOAuthClient(OAuthClient):
    counter = 0

    def __init__(self, default_oauth_token: OAuthTokens):
        self.default_oauth_token = default_oauth_token

    def refresh(self, refresh_token: str) -> OAuthTokens:
        if refresh_token == self.default_oauth_token.refresh_token:
            FakeOAuthClient.counter += 1

            new_token = OAuthTokens(
                f"new_access_token_{FakeOAuthClient.counter}",
                f"new_fresh_token_{FakeOAuthClient.counter}",
                datetime.now(timezone.utc),
            )

            self.default_oauth_token = new_token
            return new_token
        else:
            raise ValueError("Not the right refresh_token")
