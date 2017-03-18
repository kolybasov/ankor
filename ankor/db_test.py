from .db import Database


class TestDatabase:
    """ Test Database adapter. """

    def test_init(self):
        """ Test if connection is saved after creating new DB instance. """
        db = Database(':memory:')
        assert db.__connection__ is not None
        db.close()

    def test_close(self):
        """ Test if connection is removed after closing connection. """
        db = Database(':memory:')
        db.close()
        assert db.__connection__ is None

    def test_execute(self):
        """ Test if execute shorthand return result from original method. """
        db = Database(':memory:')
        result = db.execute('CREATE TABLE test (id integer primary key)')
        assert result is not None
        db.close()

    def test_multiple_connections(self):
        """ Test if all DB instances shares the same connection. """
        db1 = Database(':memory:')
        db2 = Database(':memory:')
        assert db1.__connection__ == db2.__connection__
        db1.close()
        assert db2.__connection__ is None
