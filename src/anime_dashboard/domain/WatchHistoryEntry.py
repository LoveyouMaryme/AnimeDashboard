from dataclasses import dataclass


@dataclass
class WatchHistoryEntry:
    """
    Represents a single entry in the watch history.

    Attributes:
        anime_title (str): The title of the anime.
        episode_number (int): The episode number that was retrieved.
        retrieved_at (str): The timestamp when the episode was retrieved.
        source (str): The source of the watch history entry.
    """
    anime_title: str
    episode_number: int
    source: str
    retrieved_at: str