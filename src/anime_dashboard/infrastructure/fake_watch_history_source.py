from anime_dashboard.app.watch_history_source import WatchHistorySource
from anime_dashboard.domain.watch_history_entry import WatchHistoryEntry

class FakeWatchHistorySource(WatchHistorySource):
    """
    A fake watch history source for testing purposes.
    """
    def get_watch_events(self) -> list[WatchHistoryEntry]:
        """
        Returns a list of fake watch history entries.

        Returns:
            list: A list of fake watch history entries.
        """
        return [
            WatchHistoryEntry(anime_title="Naruto", episode_number=1, source="FakeSource", watched_at="2023-01-01T12:00:00Z"),
            WatchHistoryEntry(anime_title="Naruto", episode_number=2, source="FakeSource", watched_at="2023-01-01T12:30:00Z"),
            WatchHistoryEntry(anime_title="Naruto", episode_number=3, source="FakeSource", watched_at="2023-01-01T13:00:00Z"),
            WatchHistoryEntry(anime_title="One Piece", episode_number=5, source="FakeSource", watched_at="2023-01-02T12:00:00Z"),
            WatchHistoryEntry(anime_title="Attack on Titan", episode_number=10, source="FakeSource", watched_at="2023-01-03T12:00:00Z"),
        ]