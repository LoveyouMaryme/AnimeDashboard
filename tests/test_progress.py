import pytest

from anime_dashboard.progress import should_update


def test_should_update_when_source_is_ahead():
    assert should_update(8, 5) is True


def test_should_not_update_when_source_is_behind():
    assert should_update(5, 8) is False


def test_should_not_update_when_source_is_equal():
    assert should_update(5, 5) is False


def test_should_not_update_when_source_hasnt_started():
    assert should_update(0, 0) is False


def test_0_source_isnt_an_issue():
    assert should_update(0, 1) is False


def test_0_mal_isnt_an_issue():
    assert should_update(1, 0) is True


def test_negative_source_progress():
    with pytest.raises(ValueError):
        should_update(-1, 5)


def test_negative_mal_progress():
    with pytest.raises(ValueError):
        should_update(5, -1)
