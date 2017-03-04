import config as cfg

from flask import Flask
from ankor import Database

import routes

# Connect to DB
db = Database(cfg.get('db.name', './ankor_sqlite.db'))

# Create Flask app
app = Flask(__name__)

# Router
app.route('/')(routes.root_get)

# Run server
if __name__ == '__main__':
    app.run(
        host=cfg.get('server.host', '127.0.0.1'),
        port=cfg.get('server.port', 3333)
    )
    db.close()
