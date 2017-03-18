from .base import BaseRoute
from ankor.models import Link


class LinksRoute(BaseRoute):
    def index(self):
        return str(Link.all())

    def show(self, id):
        return str(Link.find(id))
