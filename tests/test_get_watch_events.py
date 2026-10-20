import pytest

from anime_dashboard.domain.watch_history_entry import WatchHistoryEntry
from anime_dashboard.infrastructure.fake_watch_history_source import FakeWatchHistorySource


def test_get_watch_events():
    # Arrange
    fake_source = FakeWatchHistorySource()

    watched_animes = fake_source.get_watch_events()

    assert isinstance(watched_animes, list)
    assert all(isinstance(anime, WatchHistoryEntry) for anime in watched_animes)
    assert watched_animes[0].anime_title == "Naruto"
    assert sum(anime.anime_title == "Naruto" for anime in watched_animes) == 3