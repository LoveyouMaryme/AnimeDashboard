from typing import Protocol

from anime_dashboard.domain.watch_history_entry import WatchHistoryEntry



class WatchHistorySource(Protocol):
    """
    Represents the contract a watch history source 
    must fulfill to be used in the application.
    """

    def get_watch_events(self) -> list[WatchHistoryEntry]:
        """
        Fetches the watch history entries from the source.

        Returns:
            list: A list of watch history entries.
        """

        ...
        