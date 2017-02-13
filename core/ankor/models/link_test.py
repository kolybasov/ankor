from .link import Link

EXAMPLE_URL = 'http://example.org'


class TestLink:
    def test_init(self):
        link = Link(url=EXAMPLE_URL)
        assert link.media_type == 'page'
        assert link.title == 'Example Domain'
        assert link.description is None
