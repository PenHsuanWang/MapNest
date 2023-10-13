from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['gis_database']
shapefiles_collection = db['shapefiles']

def get_all_shapefiles():
    return list(shapefiles_collection.find({}, {"_id": 0, "data": 0}))

def get_shapefile_data(name):
    return shapefiles_collection.find_one({"name": name}, {"_id": 0})

def save_shapefile_to_mongodb(name, description, geojson_data):
    shapefiles_collection.insert_one({
        "name": name,
        "description": description,
        "data": geojson_data
    })
