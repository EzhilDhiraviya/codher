from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

db=None

uri = "mongodb+srv://ezhildhiraviya:e0VzJeqYvlFLra3R@dep1.lidw9jc.mongodb.net/?retryWrites=true&w=majority&appName=dep1"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['sampledb']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)