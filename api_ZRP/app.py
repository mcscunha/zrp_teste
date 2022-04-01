from flask import Flask
from flask import jsonify, Response
from dotenv import load_dotenv

from .configuration import init_app as conf_init
from .view import init_app as view_init


load_dotenv()


def create_app():
    app = Flask(__name__)
    conf_init(app)
    view_init(app)
    
    return app

