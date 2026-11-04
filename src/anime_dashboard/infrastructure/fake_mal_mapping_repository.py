from anime_dashboard.app.anime_mapping_repository import AnimeMappingRepository


class FakeMalMappingRepository(AnimeMappingRepository):
    """Store fake anime mappings for streaming platforms."""

    ANIME_REPOSITORY = [
        {"platform": "Crunchyroll", "id": 1, "mal_id": 20, "name": "Naruto"},
        {"platform": "Netflix", "id": 2, "mal_id": 21, "name": "One Piece"},
        {
            "platform": "Crunchyroll",
            "id": 3,
            "mal_id": 16498,
            "name": "Attack on Titan",
        },
        {"platform": "Netflix", "id": 4, "mal_id": 16498, "name": "Attack on Titan"},
        {
            "platform": "Crunchyroll",
            "id": 5,
            "mal_id": 5114,
            "name": "Fullmetal Alchemist: Brotherhood",
        },
        {
            "platform": "Crunchyroll",
            "id": 5,
            "mal_id": 5112,
            "name": "Fullmetal Alchemist",
        },
    ]

    def get_mal_id(self, platform_name: str, anime_id: int) -> int | None:
        """Return the anime name and MAL ID for a platform and numeric anime ID.

        Args:
            platform_name: Name of the streaming platform.
            anime_id: Numeric anime ID on that platform.

        Returns:
            A tuple containing the anime name and MAL ID, or None if not found.
        """
        matches = []
        for anime in self.ANIME_REPOSITORY:
            if anime["platform"] == platform_name and anime["id"] == anime_id:
                matches.append(anime["mal_id"])

            if len(matches) == 1:
                return matches[0]

            if len(matches) > 1:
                raise ValueError("There are duplicates or there is an ambiguity")
        return None
