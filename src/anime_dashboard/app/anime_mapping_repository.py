from typing import Protocol


class AnimeMappingRepository(Protocol):
    """
    Get the Id of an Anime in a target Platform  (dictionnary)from
    the Id of Anime comign from a source Platform (streaming)

    """

    def get_mal_id(self, platform_name: str, anime_id: int) -> int | None:
        """Find the MyAnimeList (MAL) mapping for a source platform anime ID.

        Args:
            platform_name: Name of the streaming platform.
            anime_id: Numeric anime ID on that platform.

        Returns:
            A tuple containing the anime name and its MAL ID, or None
            if no mapping is found.
        """
        ...
