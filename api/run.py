import yaml
import io

from flask import Flask

# Parse config
config = yaml.load(io.open('./config.yml', 'r'))

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
