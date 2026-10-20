from typing import Protocol

from src.domain.WatchHistoryEntry import WatchHistoryEntry


@Protocol
class WatchHistorySource(Protocol):
    """
    Represents the contract a watch history source 
    must fulfill to be used in the application.

    Every hour or whenever the user clicks the "Refresh" button, 
    the application will get the watch history from each registered source.
    """

    def get_watch_events(self) -> list[WatchHistoryEntry]:
        """
        Fetches the watch history entries from the source.

        Args:
            None

        Returns:
            list: A list of watch history entries.
        """

        return NotImplemented
        