from anime_dashboard.app.anime_mapping_repository import AnimeMappingRepository


class FakeMalMappingRepository(AnimeMappingRepository):
    """
    Exposing a fake anime repository

    """

    ANIME_REPOSITORY = {
        "CR_001": 20,  # Naruto
        "NET_002": 21,  # One Piece
        "CR_003": 16498,  # Attack on Titan
        "NET_004": 16498,  # Attack on Titan
        "CR_005": 5114,  # Fullmetal Alchemist: Brotherhood}
    }

    def get_mal_id(self, anime_id: str) -> int:
        """
        Search mal anime id from any streaming platform id in our dictionnary

        args :
            anime_id : ID from any streaming platform

        return :
            MAL anime id if found, otherwise None

        """

        mal_id = self.ANIME_REPOSITORY.get(anime_id)

        if mal_id:
            return mal_id
        else:
            return None
