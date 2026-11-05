from datetime import datetime, timedelta, timezone

import pytest

from anime_dashboard.app.default_token_provider import DefaultTokenProvider
from anime_dashboard.infrastructure.fake_token_storage import FakeTokenStorage
from anime_dashboard.infrastructure.oauth_token import OAuthTokens
from tests.fakes import FakeOAuthClient

auth = OAuthTokens(
    "access_token",
    "fresh_token",
    datetime.now(timezone.utc) - timedelta(days=1),
)


def test_no_first_token():
    token_provider = DefaultTokenProvider(FakeOAuthClient(auth), None)

    with pytest.raises(ValueError):
        token_provider.get_access_token()


def test_expiration_date_after():
    token_provider = DefaultTokenProvider(
        FakeOAuthClient(auth),
        FakeTokenStorage(
            OAuthTokens(
                "access_token",
                "fresh_token",
                datetime.now(timezone.utc) + timedelta(days=1),
            )
        ),
    )

    access_token = token_provider.get_access_token()
    assert access_token == "access_token"


def test_expiration_date_before():
    token_provider = DefaultTokenProvider(FakeOAuthClient(auth), FakeTokenStorage(auth))

    access_token = token_provider.get_access_token()
    assert access_token == "new_access_token_1"
