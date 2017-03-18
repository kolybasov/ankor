from .google import GoogleProvider

TEST_URL = 'https://example.org'


class TestGoogleProvider:
    def test_short(self):
        provider = GoogleProvider()

        assert provider.short(TEST_URL).startswith('https://goo.gl')
