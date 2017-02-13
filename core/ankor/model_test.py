from .model import Model


class ExampleModel(Model):
    @classmethod
    def create_test_table(cls):
        cls.__db__.execute("""CREATE TABLE example_models (
            id INTEGER PRIMARY KEY,
            test TEXT,
            test1 TEXT
        )""")

    @classmethod
    def drop_test_table(cls):
        cls.__db__.execute('DROP TABLE example_models')


class TestModel:
    def setup_method(self, method):
        ExampleModel.create_test_table()

    def teardown_method(self, method):
        ExampleModel.drop_test_table()

    def test_create_tablename(self):
        model = ExampleModel()
        assert model.__tablename__ == 'example_models'

    def test_create_placeholders(self):
        model = ExampleModel()
        assert model.__create_placeholders__() == '?,?,?'
        assert model.__create_placeholders__(with_names=True) == 'id=?,'\
            'test=?,'\
            'test1=?'

    def test_collect_values(self):
        model = ExampleModel(test='test', test1='test1')
        assert model.__collect_values__() == (None, 'test', 'test1')

    def test_init(self):
        model = ExampleModel(id=1)
        assert model.id == 1

    def test_create(self):
        model = ExampleModel(test='test', test1='test1')
        model.__create__()
        assert model.id is not None

    def test_update(self):
        model = ExampleModel(test='test', test1='test1')
        model.__create__()

        model.test = '10'
        model.__update__()

        row = model.__db__.execute('SELECT * FROM example_models').fetchone()

        assert row['test'] == '10'

    def test_find(self):
        model = ExampleModel(test='test', test1='test1')
        model.save()
        assert ExampleModel.find(model.id).id == model.id

    def test_all(self):
        model = ExampleModel(test='test', test1='test1')
        model1 = ExampleModel(test='test', test1='test1')

        model.save()
        model1.save()

        assert len(ExampleModel.all()) == 2
