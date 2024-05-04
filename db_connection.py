# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# def get_mongo_client():
#     uri = "mongodb+srv://ezhildhiraviya:qioUxc0iE44VIH7X@cluster0.3jdgkoz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#     try:
#         client = MongoClient(uri, server_api=ServerApi('1'))
#         client.admin.command('ping')  # Send a ping to confirm a successful connection
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#         return client
#     except Exception as e:
#         print("Failed to connect to MongoDB:", e)
#         return None


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_mongo_client():
    uri = "mongodb+srv://ezhildhiraviya:qioUxc0iE44VIH7X@cluster0.3jdgkoz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')  # Send a ping to confirm a successful connection
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print("Failed to connect to MongoDB:", e)
        return None

def get_locations_collection():
    client = get_mongo_client()
    if client:
        db = client['sports']  # Connect to the 'sports' database
        return db.centres  # Return the 'centres' collection
    else:
        return None

