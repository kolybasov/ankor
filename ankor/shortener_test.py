from .shortener import Shortener


class TestShortener:
    def test_short(self):
        shortener = Shortener('https://mbasov.me')

        assert shortener.short().startswith('https://goo.gl')
