from datetime import datetime, timedelta, timezone

import pytest

from anime_dashboard.infrastructure.oauth_token import OAuthTokens
from tests.fakes import FakeOAuthClient


def test_counter_zero():
    assert (
        FakeOAuthClient(
            OAuthTokens(
                "access_token",
                "fresh_token",
                datetime.now(timezone.utc) - timedelta(days=1),
            )
        ).counter
        == 0
    )


def test_counter_one():
    fake_OAuth = FakeOAuthClient(
        OAuthTokens(
            "access_token",
            "fresh_token",
            datetime.now(timezone.utc) - timedelta(days=1),
        )
    )

    fake_OAuth.refresh("fresh_token")
    assert fake_OAuth.counter == 1


def test_counter_two():
    fake_OAuth = FakeOAuthClient(
        OAuthTokens(
            "access_token",
            "fresh_token",
            datetime.now(timezone.utc) - timedelta(days=1),
        )
    )

    fake_OAuth.refresh("fresh_token")
    fake_OAuth.refresh("new_fresh_token_1")
    assert fake_OAuth.counter == 2


def test_error_bad_token():
    fake_OAuth = FakeOAuthClient(
        OAuthTokens(
            "access_token",
            "fresh_token",
            datetime.now(timezone.utc) - timedelta(days=1),
        )
    )

    fake_OAuth.refresh("fresh_token")
    with pytest.raises(ValueError):
        fake_OAuth.refresh("new_fresh_token_")


def test_counter_two_instance():
    fake_OAuth_a = FakeOAuthClient(
        OAuthTokens(
            "access_token_a",
            "fresh_token_a",
            datetime.now(timezone.utc) - timedelta(days=1),
        )
    )
    fake_OAuth_b = FakeOAuthClient(
        OAuthTokens(
            "access_token_b",
            "fresh_token_b",
            datetime.now(timezone.utc) - timedelta(days=1),
        )
    )

    fake_OAuth_a.refresh("fresh_token_a")
    assert fake_OAuth_b.counter == 0
