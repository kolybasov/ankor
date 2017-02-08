import yaml
import io

from flask import Flask

from ankor.db import Database

# Parse config
config = yaml.load(io.open('./config.yml', 'r'))

# Connect to DB
db = Database(config['db']['name'])

# Create Flask app
app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Ankor!'


# Run server
if __name__ == '__main__':
    app.run(
        host=config['server']['host'],
        port=config['server']['port']
    )
