from datetime import datetime

from anime_dashboard.infrastructure.fake_token_storage import FakeTokenStorage
from anime_dashboard.infrastructure.oauth_token import OAuthTokens


def test_load_nothing():
    storage = FakeTokenStorage()
    assert storage.load() is None


def test_load_token():
    auth = OAuthTokens(
        "actual_token", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0))
    )
    storage = FakeTokenStorage(auth)
    assert storage.load() == OAuthTokens(
        "actual_token", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0))
    )


def test_save_token():
    storage = FakeTokenStorage(
        OAuthTokens(
            "actual_token", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0))
        )
    )
    assert storage.load() == "123"
    storage.save(
        OAuthTokens("new_token", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0)))
    )
    assert storage.load() == OAuthTokens(
        "new_token", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0))
    )


def test_different_storage():
    storage_a = FakeTokenStorage(
        OAuthTokens("a", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0)))
    )
    storage_b = FakeTokenStorage(
        OAuthTokens("b", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0)))
    )
    assert storage_a.load() == OAuthTokens(
        "a", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0))
    )
    assert storage_b.load() == OAuthTokens(
        "b", "refresh_token", (datetime(9999, 12, 31, 00, 00, 0))
    )
