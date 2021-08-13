import os
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config['CANCION_RESOURCE_URL'] = os.getenv('CANCION_RESOURCE_URL', 'http://127.0.0.1:5000/cancion/{}')
    return app