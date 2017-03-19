from .base import BaseRoute
from flask import render_template, request, flash, redirect
from ankor.models import Settings


class SettingsRoute(BaseRoute):
    def index(self):
        providers = [
            {'id': 'google', 'name': 'Google', 'url': 'https://goo.gl'}
        ]

        # get settings or create default  is not present
        settings = Settings.all()
        if len(settings) == 0:
            settings = Settings()
            settings.save()
        else:
            settings = settings[0]

        return render_template(
            'settings.html',
            settings=settings,
            providers=providers
        )

    def create(self):
        id = request.form.get('settings_id', None)
        api_provider = request.form.get('api_provider', None)
        short_all_links = request.form.get('short_all_links', 0)

        settings = Settings.find(id)
        settings.api_provider = api_provider
        settings.short_all_links = short_all_links
        settings.save()

        flash(u'Settings saved.', 'success')

        return redirect('settings')
