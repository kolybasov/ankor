from abc import ABC
from .db import Database
from inflection import underscore, pluralize


def dict_from_row(row):
    return dict(zip(row.keys(), row))


class Model(ABC):
    """ Abstract model class to work with DB entities as objects. """

    __db__ = Database()
    __primary_key__ = 'id'
    __schema__ = []

    def __init__(self, **kwargs):
        """ Create new model instance. """
        # Create table name from child class name
        self.__create_tablename__()

        # Get table schema from DB if it is not present yet
        if len(self.__schema__) == 0:
            schema_query = 'PRAGMA table_info({})'.format(self.__tablename__)
            schema = self.__db__.execute(schema_query)

            for field in schema.fetchall():
                field_name = field['name']
                self.__schema__.append(field_name)
                setattr(self, field_name, kwargs.get(field_name, None))
        else:
            for field in self.__schema__:
                setattr(self, field, kwargs.get(field, None))

    @classmethod
    def __create_tablename__(cls):
        """ Take child class name, lowercase and pluralize it. """
        class_name = cls.__name__
        tablename = underscore(pluralize(class_name))

        cls.__tablename__ = tablename

    def __create_placeholders__(self, with_names=False):
        """ Create placeholders for SQL queries like INSERT or UPDATE. """
        if with_names:
            def collect_func(key):
                return '{}=?'.format(key)
        else:
            def collect_func(key):
                return '?'

        placeholders = [collect_func(f) for f in self.__schema__]

        return ','.join(placeholders)

    def __collect_values__(self):
        """ Collection current model values to tuple. """
        values = map(lambda f: getattr(self, f), self.__schema__)

        return tuple(values)

    def __create__(self):
        """ Create new record in database. """

        placeholders = self.__create_placeholders__()
        values = self.__collect_values__()

        query = 'INSERT INTO `{}` VALUES ({})'.format(
            self.__tablename__,
            placeholders
        )

        result = self.__db__.execute(query, values)

        last_id = result.lastrowid
        setattr(self, self.__primary_key__, last_id)

        return result

    def __update__(self):
        """ Update existing record in database. """

        primary_key_val = getattr(self, self.__primary_key__)

        values = self.__collect_values__()
        placeholders = self.__create_placeholders__(with_names=True)

        query = """UPDATE {table}
        SET {placeholders}
        WHERE {primary_key_name}={primary_key_val}""".format(
            table=self.__tablename__,
            placeholders=placeholders,
            primary_key_name=self.__primary_key__,
            primary_key_val=primary_key_val
        )

        return self.__db__.execute(query, values)

    def save(self):
        """ Update existing record or create new. """
        if getattr(self, self.__primary_key__) is None:
            return self.__create__()
        else:
            return self.__update__()

    @classmethod
    def find(cls, pk):
        """ Find record by primary key and return new instance or None
        if nothing was found. """

        query = """SELECT *
        FROM {table}
        WHERE {primary_key_name}=?""".format(
            table=cls.__tablename__,
            primary_key_name=cls.__primary_key__
        )

        result = cls.__db__.execute(query, (pk,))
        record = result.fetchone()

        if record is not None:
            fields = dict_from_row(record)

            return cls(**fields)
        else:
            return None

    @classmethod
    def all(cls):
        """ Find all records of this type. """

        query = 'SELECT * FROM {}'.format(cls.__tablename__)

        result = cls.__db__.execute(query)

        records = result.fetchall()

        if len(records) == 0:
            return records
        else:
            return [cls(**dict_from_row(r)) for r in records]
