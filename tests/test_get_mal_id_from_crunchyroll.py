import random
from collections import Counter

from anime_dashboard.infrastructure.fake_mal_mapping_repository import (
    FakeMalMappingRepository,
)

FAKE_ANIME_REPO = FakeMalMappingRepository()
repository = FAKE_ANIME_REPO.ANIME_REPOSITORY


def test_anime_found():
    assert FAKE_ANIME_REPO.get_mal_id("CR_001") == 20
    assert FAKE_ANIME_REPO.get_mal_id("CR_001") == 20


def test_anime_not_found():
    assert FAKE_ANIME_REPO.get_mal_id("Ca existe pas") is None


def test_different_source_id():
    duplicate_values = []
    values = repository.values()

    for value, count in Counter(values).items():
        if count > 1:
            duplicate_values.append(value)

    duplicate_value = random.choice(duplicate_values)

    source_ids = [
        source_id
        for source_id, mal_id in repository.items()
        if mal_id == duplicate_value
    ]
    assert len(source_ids) == len(set(source_ids))


def test_unique_source_id():
    assert len(repository) == len(set(repository))
