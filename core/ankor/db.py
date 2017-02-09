import sqlite3


class Database:
    """ DB adapter. """

    """ Link to opened connection. """
    __connection__ = None

    def __init__(self, db=':memory:'):
        """ Open new connection and save link to it. Ensure only one connection
        is open all the time.
        """
        if self.__class__.__connection__ is None:
            self.__class__.__connection__ = sqlite3.connect(db)

    def execute(self, *args):
        """ Shorthand for sqlite3.Connection.execute method. """
        return self.__class__.__connection__.execute(*args)

    def close(self):
        """ Close DB connection and remove links to it. """
        self.__class__.__connection__.close()
        self.__class__.__connection__ = None
