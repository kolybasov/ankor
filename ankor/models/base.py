from abc import ABC
from inflection import underscore, pluralize


class BaseModel(ABC):
    """ Abstract model class to work with DB entities as objects. """

    __primary_key__ = 'id'

    def __init__(self, **kwargs):
        """ Create new model instance. """
        for field in self.__class__.__schema__:
            default_val = getattr(self, field, None)
            field_val = kwargs.get(field, default_val)
            if field_val is not None:
                setattr(self, field, field_val)
            else:
                setattr(self, field, None)

    @classmethod
    def __setup__(cls, db):
        """ Should be called before using other methods. """
        cls.__db__ = db
        cls.__create_tablename__()
        cls.__fetch_schema__()

    @classmethod
    def __fetch_schema__(cls):
        """ Fetch DB schema and set attrs. """
        if not hasattr(cls, '__schema__'):
            # Create fields list shared among all instances
            setattr(cls, '__schema__', [])

            # Ask DB for table schema
            schema_query = 'PRAGMA table_info({})'.format(cls.__tablename__)
            result = cls.__db__.execute(schema_query)

            for field in result.fetchall():
                # Get each field name and default value
                field_name = field['name']
                field_val = field['dflt_value']

                cls.__schema__.append(field_name)
                setattr(cls, field_name, field_val)

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
        self.__db__.__connection__.commit()

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

        self.__db__.execute(query, values)
        return self.__db__.__connection__.commit()

    def save(self):
        """ Update existing record or create new. """
        if getattr(self, self.__primary_key__) is None:
            return self.__create__()
        else:
            return self.__update__()

    def destroy(self):
        """ Delete record from databse. """

        query = 'DELETE FROM {table} WHERE {pk_name}={pk_val}'.format(
            table=self.__tablename__,
            pk_name=self.__primary_key__,
            pk_val=getattr(self, self.__primary_key__)
        )

        self.__db__.execute(query)
        return self.__db__.__connection__.commit()

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
            fields = dict(record)

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
            return [cls(**dict(r)) for r in records]

    @classmethod
    def query(cls, query, *args):
        """ Allow custom queries. """

        query = query.format(table=cls.__tablename__)

        result = cls.__db__.execute(query, *args)

        records = result.fetchall()

        if len(records) == 0 or 'id' not in records[0].keys():
            return records
        else:
            return [cls(**dict(r)) for r in records]
