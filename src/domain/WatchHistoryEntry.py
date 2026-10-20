from dataclasses import dataclass


@dataclass
class WatchHistoryEntry:
    """
    Represents a single entry in the watch history.

    Attributes:
        anime_id (int): The unique identifier of the anime.
        anime_title (str): The title of the anime.
        episode_number (int): The episode number that was watched.
        retrieved_at (str): The timestamp when the episode was watched.
        source (str): The source of the watch history entry.
    """
    anime_id: int
    anime_title: str
    episode_number: int
    source: str
    retrieved_at: str