from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = [
    {
        'host': 'localhost',
        'port': 27017,
        'db': 'test_db2'
    }
]

app.secret_key = "2g3hjkrfhjk34hj"  # necessary for the session cookie

my_db = MongoEngine(app)

class User(my_db.Document):
    meta = {
        "collection": "appUser"
    }
    email = my_db.StringField(required=True)
    name = my_db.StringField(max_length=50)

user1 = User(
    email = "admin@abc.com",
    name = "admin"
)

user1.save()