#!/usr/bin/env python3

import config as cfg

from flask import Flask
from ankor import Database
from ankor import models
from routes import (
    LinksRoute,
    RootRoute
)

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
    '/links/<id>',
    'links',
    links_route.call,
    methods=['GET', 'PUT', 'DELETE']
)

# Run server
if __name__ == '__main__':
    app.run(
        host=cfg.get('server.host', '127.0.0.1'),
        port=cfg.get('server.port', 3333)
    )
    db.close()
