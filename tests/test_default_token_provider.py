from datetime import datetime, timedelta, timezone

import pytest

from anime_dashboard.app.default_token_provider import DefaultTokenProvider
from anime_dashboard.infrastructure.fake_token_storage import FakeTokenStorage
from anime_dashboard.infrastructure.oauth_token import OAuthTokens
from tests.fakes import FakeOAuthClient

default_auth = OAuthTokens(
    "access_token",
    "fresh_token",
    datetime.now(timezone.utc) - timedelta(days=1),
)


def test_no_storage():
    token_provider = DefaultTokenProvider(FakeOAuthClient(default_auth), None)

    with pytest.raises(ValueError):
        token_provider.get_access_token()


def test_no_access_token():
    token_provider = DefaultTokenProvider(
        FakeOAuthClient(default_auth), FakeTokenStorage(None)
    )

    with pytest.raises(ValueError):
        token_provider.get_access_token()


def test_expiration_date_after():
    auth = FakeOAuthClient(default_auth)
    token_provider = DefaultTokenProvider(
        auth,
        storage=FakeTokenStorage(
            OAuthTokens(
                "access_token",
                "fresh_token",
                datetime.now(timezone.utc) + timedelta(days=1),
            )
        ),
    )

    access_token = token_provider.get_access_token()
    assert access_token == "access_token"
    assert auth.counter == 0


def test_expiration_date_before():
    token_provider = DefaultTokenProvider(
        FakeOAuthClient(default_auth), FakeTokenStorage(default_auth)
    )

    access_token = token_provider.get_access_token()
    assert access_token == "new_access_token_1"


def test_new_token_in_storage():
    storage = FakeTokenStorage(default_auth)
    auth_client = FakeOAuthClient(default_auth)
    token_provider = DefaultTokenProvider(auth_client, storage)

    token_provider.get_access_token()

    # The same fake token that is returned by FakeOAuthClient
    assert storage.load() == auth_client.default_oauth_token

    assert storage.load() != default_auth
