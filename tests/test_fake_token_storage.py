from anime_dashboard.infrastructure.fake_token_storage import FakeTokenStorage


def test_load_nothing():
    storage = FakeTokenStorage()
    assert storage.load() is None


def test_load_token():
    storage = FakeTokenStorage("123")
    assert storage.load() == "123"


def test_save_token():
    storage = FakeTokenStorage("123")
    assert storage.load() == "123"
    storage.save("456")
    assert storage.load() == "456"


def test_different_storage():
    storage_a = FakeTokenStorage("a")
    storage_b = FakeTokenStorage("b")
    assert storage_a.load() == "a"
    assert storage_b.load() == "b"
