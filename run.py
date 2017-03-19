#!/usr/bin/env python3

import config as cfg

import sqlite3
import logging
from flask import Flask
from ankor import Database
from ankor import models, ClipboardMonitor
from ankor.models import Settings, Link
from routes import (
    LinksRoute,
    RootRoute,
    SettingsRoute
)

# Suppress flask logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Connect to DB
db = Database(cfg.get('db.name', './ankor_sqlite.db'))

# Prepare models
models.setup(db)

# Create Flask app
app = Flask(__name__)

# Set secret
app.config.update(dict(
    SECRET_KEY='development'
))

# Router
root_route = RootRoute(app)
links_route = LinksRoute(app)
settings_route = SettingsRoute(app)

# /
app.add_url_rule(
    '/',
    'index',
    root_route.call
)

# /links
app.add_url_rule(
    '/links',
    'links',
    links_route.call,
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/links/<int:id>',
    'links',
    links_route.call,
    methods=['GET', 'PUT', 'DELETE']
)
app.add_url_rule(
    '/settings',
    'settings',
    settings_route.call,
    methods=['GET', 'POST']
)


# Run clipboard monitor
def cb_reporter(content):
    print('Clipboard content: {}'.format(content))

    if (content is None or
            not content.startswith('http') or
            len(content) < 30):
        print('Cannot short it. Skipping…')
        return

    try:
        settings = Settings.default()
        link = Link(url=content)
        if settings.short_all_links == 1:
            link.short(settings.api_provider)
        else:
            link.save()
        print('Created new record!')
    except (sqlite3.IntegrityError):
        print('URL: "{}" is already exists.'.format(content))
        return


cb_monitor = ClipboardMonitor(cb_reporter)
cb_monitor.start()

# Run server
if __name__ == '__main__':
    host = cfg.get('server.host', '127.0.0.1')
    port = cfg.get('server.port', 3333)

    print('\n************************')
    print('Starting ankor server. http://{}:{}'.format(host, port))
    print('************************\n')
    app.run(host=host, port=port)

    print('\n************************')
    print('Sutting down ankor… Bye!')
    print('************************\n')

    cb_monitor.stop()
    db.close()
