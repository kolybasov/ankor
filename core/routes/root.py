from .base import BaseRoute


class RootRoute(BaseRoute):
    def index(self):
        return 'Ankor!'
