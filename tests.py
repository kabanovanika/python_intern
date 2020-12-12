import requests

from app.app import is_alive_host


class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code


class MockGet:
    def __init__(self, status_code):
        self.status_code = status_code

    def __call__(self, *args, **kwargs):
        return MockResponse(self.status_code)


def test_up_host(monkeypatch):
    monkeypatch.setattr(requests, "get", MockGet(200))
    assert is_alive_host('???')


def test_down_host(monkeypatch):
    monkeypatch.setattr(requests, "get", MockGet(400))
    assert not is_alive_host('???')
