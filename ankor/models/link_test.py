from .link import Link
from ..db import Database

EXAMPLE_URL = 'http://example.org'


class TestLink:
    @classmethod
    def setup_method(cls):
        cls.__db__ = Database()
        cls.__db__.execute("""CREATE TABLE links(
            id INTEGER PRIMARY KEY,
            url TEXT(255) NOT NULL UNIQUE,
            title TEXT(100),
            description TEXT(255),
            media_type TEXT(20),
            short_url TEXT(30)
        )""")
        Link.__setup__(cls.__db__)

    @classmethod
    def teardown_method(cls):
        cls.__db__.execute('DROP TABLE links')

    def test_init(self):
        link = Link(url=EXAMPLE_URL)
        assert link.media_type == 'page'
        assert link.title == 'Example Domain'
        assert link.description is None

    def test_short(self):
        link = Link(url=EXAMPLE_URL)

        assert link.short().startswith('https://goo.gl')
