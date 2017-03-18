from .base import BaseRoute
from flask import Flask


class NewRoute(BaseRoute):
    def index(self):
        return 'index'

    def show(self, id):
        return id

    def create(self):
        return 'create'

    def update(self, id):
        return 'update'


class TestBaseRoute:
    @classmethod
    def setup_class(cls):
        app = Flask(__name__)
        test_route = NewRoute(app)

        app.add_url_rule(
            '/',
            'index',
            test_route.call,
            methods=['GET', 'POST']
        )
        app.add_url_rule(
            '/<id>',
            'index',
            test_route.call,
            methods=['GET', 'PUT', 'DELETE']
        )

        cls.app = app
        cls.test_route = test_route

    def test_init(self):
        assert self.test_route.env is not None

    def test_actions(self):
        with self.app.test_client() as c:
            index_res = c.get('/')
            assert 'index' in str(index_res.data)

            show_res = c.get('/10')
            assert '10' in str(show_res.data)

            create_res = c.post('/')
            assert 'create' in str(create_res.data)

            update_res = c.put('/10')
            assert 'update' in str(update_res.data)

            delete_res = c.delete('/10')
            assert delete_res.status_code == 500
