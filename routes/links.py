from .base import BaseRoute
from ankor.models import Link
from flask import render_template, request

PER_PAGE = 15


class LinksRoute(BaseRoute):
    def index(self):
        if request.args.get('filter', None) is None:
            query = """
                SELECT *
                FROM {table}
                ORDER BY created_at DESC
                LIMIT ?
                OFFSET ?
            """
        else:
            query = """
                SELECT *
                FROM {table}
                WHERE short_url IS NOT NULL
                ORDER BY created_at DESC
                LIMIT ?
                OFFSET ?
            """

        page = request.args.get('page', '1')
        offset = (int(page) - 1) * PER_PAGE

        links = Link.query(query, (PER_PAGE, offset))

        return render_template(
            'links/index.html',
            links=links,
            fetch_more=(PER_PAGE == len(links))
        )

    def show(self, id):
        return str(Link.find(id))
