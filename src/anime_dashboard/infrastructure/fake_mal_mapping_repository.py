from anime_dashboard.app.anime_mapping_repository import AnimeMappingRepository


class FakeMalMappingRepository(AnimeMappingRepository):
    """
    Exposing a fake anime repository


    """

    def get_mal_id(self, anime_id: str) -> int | None:
        # This would be an external database
        ANIME_REPOSITORY = {
            "CR_001": 20,  # Naruto
            "CR_002": 21,  # One Piece
            "CR_003": 16498,  # Attack on Titan
            "CR_004": 30230,  # One Punch Man
            "CR_005": 5114,  # Fullmetal Alchemist: Brotherhood}
        }

        """
        Search mal anime id from crunchyroll id in our dictionnary
        
        args :
            crunchyroll_id : ID from streaming platfrom Crunchyroll

        return :
            MAL anime id if found, otherwise None
            
        """

        mal_id = ANIME_REPOSITORY.get(anime_id)

        if mal_id:
            return mal_id
        else:
            return None
