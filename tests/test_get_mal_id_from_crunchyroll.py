import pytest

from anime_dashboard.infrastructure.fake_mal_mapping_repository import (
    FakeMalMappingRepository,
)

FAKE_ANIME_REPO = FakeMalMappingRepository()
repository = FAKE_ANIME_REPO.ANIME_REPOSITORY


def test_anime_found():
    assert FAKE_ANIME_REPO.get_mal_id("Crunchyroll", 1) == 20
    assert FAKE_ANIME_REPO.get_mal_id("Netflix", 2) == 21


def test_anime_not_found():
    assert FAKE_ANIME_REPO.get_mal_id("Crunchyroll", 999) is None
    assert FAKE_ANIME_REPO.get_mal_id("Netflix", 1) is None


def test_different_source_id():
    assert FAKE_ANIME_REPO.get_mal_id("Crunchyroll", 3) == 16498
    assert FAKE_ANIME_REPO.get_mal_id("Netflix", 4) == 16498


def test_ambiguous_mapping():
    with pytest.raises(ValueError):
        FAKE_ANIME_REPO.get_mal_id("Crunchyroll", 5)
