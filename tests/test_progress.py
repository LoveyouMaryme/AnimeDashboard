from anime_dashboard.progress import Progress
import pytest


def test_should_update_when_source_is_ahead():
    progress = Progress(8, 5)

    assert progress.should_update() is True

def test_should_not_update_when_source_is_behind():

    assert Progress(5, 8).should_update() is False

def test_should_not_update_when_source_is_equal():

    assert Progress(5, 5).should_update() is False

def test_should_not_update_when_source_hasnt_started():

    assert Progress(0, 0).should_update() is False

def test_negative_source_progress():
    with pytest.raises(ValueError):
        Progress(-1, 5).should_update()

def test_negative_mal_progress():
    with pytest.raises(ValueError):
        Progress(5, -1).should_update()