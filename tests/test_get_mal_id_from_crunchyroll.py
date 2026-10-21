from anime_dashboard.infrastructure.fake_mal_mapping_repository import (
    FakeMalMappingRepository,
)

FAKE_ANIME_REPO = FakeMalMappingRepository()


def test_anime_found():
    assert FAKE_ANIME_REPO.get_mal_id_from_crunchyroll("CR_001") == 20


def test_anime_not_found():
    assert FAKE_ANIME_REPO.get_mal_id_from_crunchyroll("Ca existe pas") is None
