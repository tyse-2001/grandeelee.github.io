from flask import Flask
from flask_mongoengine import MongoEngine


def create_app():
    app = Flask(__name__)  #__name__ = __main__
    app.secret_key = "2g3hjkrfhjk34hj"  # necessary for the session cookie

    app.config['MONGODB_SETTINGS'] = [
        {
            'host': 'localhost',
            'port': 27017,
            'db': 'my_db'
        }
    ]

    my_db = MongoEngine(app)
    return app, my_db

app, my_db = create_app()