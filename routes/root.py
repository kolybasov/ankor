from .base import BaseRoute
from flask import render_template
from ankor.models import Link


class RootRoute(BaseRoute):
    def index(self):
        linksCount = Link.query(
            'SELECT COUNT(*) as count FROM {table}'
        )[0]['count']
        shortLinksCount = Link.query(
            'SELECT COUNT(*) as count FROM {table} WHERE short_url IS NOT NULL'
        )[0]['count']

        return render_template(
            'index.html',
            linksCount=linksCount,
            shortLinksCount=shortLinksCount
        )
