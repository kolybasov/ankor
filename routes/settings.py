from .base import BaseRoute
from flask import render_template


class SettingsRoute(BaseRoute):
    def index(self):
        return render_template('settings.html')
