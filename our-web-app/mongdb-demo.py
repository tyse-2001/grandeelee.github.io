from pymongo import MongoClient

CONNECT_STRING = "mongodb://localhost:27017"
client = MongoClient(CONNECT_STRING)
my_db = client["test_db"]

my_collection = my_db['test_collection']

item_1 = {
    "_id": "234284",
    "name": "blender",
    "price": "99",
    "category": "appliance"
}
item_2 = {
    "_id": "234245",
    "name": "egg",
    "price": "2",
    "category": "food"
}

my_collection.insert_many([item_1, item_2])