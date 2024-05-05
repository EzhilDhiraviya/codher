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
    
def get_students_from_locations_collection():
    client = get_mongo_client()
    if client:
        db = client['your_database_name']  # Replace 'your_database_name' with your actual database name
        locations_collection = db['locations_collection']  # Replace 'locations_collection' with your actual collection name
        student_records = []
        for location in locations_collection.find({}):
            student_records.extend(location.get('students', []))
        return student_records
    else:
        return None
    

def get_sdats():
    client = get_mongo_client()
    if client:
        db = client['sports']  # Connect to the 'sports' database
        cursor = db.sdats  
        cursor = db.sdats.find({}, {'_id': 0})  # Exclude the '_id' field from the result
        sdats = [sdat for sdat in cursor]
        sdats_values = [list(sdat.values()) for sdat in sdats]
        print(sdats_values)
        return sdats_values
    else:
        return None
    
def get_records_by_sdat(sdat_value):
    client = get_mongo_client()
    if client:
        db = client['sports']  # Connect to the 'sports' database
        collection = db['students']  # Assuming the collection name is 'students', change if needed
        cursor = collection.find({}, {'_id': 0})  # Exclude the '_id' field from the result
        # records = [record for record in cursor]
        # print(records)
        matching_records = list(collection.find({"sdat": sdat_value}))
        for record in matching_records:
            record.pop('_id', None)  # Remove the _id field from each document
        if matching_records:
            print("Matching records:")
            for record in matching_records:
                print(record)
        else:
            print("No matching records found.")
        return matching_records
    else:
        return None
