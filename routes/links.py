from .base import BaseRoute
from ankor.models import Link, Settings
from flask import render_template, request, redirect, flash
from xerox import copy

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

        page = int(request.args.get('page', '1'))
        offset = (page - 1) * PER_PAGE

        links = Link.query(query, (PER_PAGE, offset))

        return render_template(
            'links/index.html',
            links=links,
            fetch_more=(PER_PAGE == len(links)),
            fetch_previous=(page > 1),
            page=page
        )

    def create(self):
        id = request.form.get('link_id', None)
        action = request.form.get('action', 'short')
        link = Link.find(id)

        if action == 'short':
            if link.short_url is None:
                settings = Settings.all()
                if len(settings) == 0:
                    settings = Settings()
                    settings.save()
                else:
                    settings = settings[0]

                link.short(settings.api_provider)

            copy(link.short_url)
            flash(
                u'Link has been shortened and copied to clipboard. {}'.format(
                    link.short_url
                ),
                'success'
            )
        elif action == 'delete':
            link.destroy()
            flash(u'Link has been deleted.', 'warning')

        return redirect('links')
