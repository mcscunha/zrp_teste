from os import getenv, urandom, path
from base64 import b64encode


def init_app(app):
    
    # Flask configuration
    key = urandom(64)
    app.config['SECRET'] = b64encode(key).decode('utf-8')
    app.config['TEMPLATE_FOLDER'] = path.join(path.dirname(path.abspath(__file__)), 'templates')
    app.config['ROOT_DIR'] = path.dirname(path.abspath(__file__))
    app.config['CSRF_ENABLE'] = getenv('CSRF_ENABLE')
    app.config['FLASK_DEBUG'] = getenv('FLASK_DEBUG')
    app.config['FLASK_ENV'] = getenv('FLASK_ENV')
    app.config['FLASK_APP'] = getenv('FLASK_APP')
    
