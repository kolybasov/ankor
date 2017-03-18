from .base import BaseRoute
from ankor.models import Link
from flask import render_template


class LinksRoute(BaseRoute):
    def index(self):
        links = Link.all()
        return render_template('links/index.html', links=links)

    def show(self, id):
        return str(Link.find(id))
