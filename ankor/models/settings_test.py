from .settings import Settings
from ..db import Database


class TestSettings:
    @classmethod
    def setup_method(cls):
        cls.__db__ = Database()
        cls.__db__.execute("""CREATE TABLE settings(
          id INTEGER PRIMARY KEY,
          listen_clipboard NUMERIC(1) NOT NULL DEFAULT 1,
          start_at_login NUMERIC(1) NOT NULL DEFAULT 0,
          short_all_links NUMERIC(1) NOT NULL DEFAULT 0,
          api_provider TEXT(20) NOT NULL DEFAULT google
        )""")
        Settings.__setup__(cls.__db__)

    @classmethod
    def teardown_method(cls):
        cls.__db__.execute('DROP TABLE settings')

    def test_init(self):
        settings = Settings()
        settings.save()

        assert settings.listen_clipboard == '1'
        assert settings.start_at_login == '0'
        assert settings.short_all_links == '0'
        assert settings.api_provider == 'google'
