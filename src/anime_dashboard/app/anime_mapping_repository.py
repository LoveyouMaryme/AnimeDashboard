from typing import Protocol


class AnimeMappingRepository(Protocol):
    """
    Get the Id of an Anime in a target Platform  (dictionnary)from
    the Id of Anime comign from a source Platform (streaming)

    """

    def get_mal_id(self, anime_id: str) -> int:
        """
        Fetches a mal ID with a correspondible anime_id

        Returns:
            int : mal_id
        """
        ...
