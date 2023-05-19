from pymongo import MongoClient, ReadPreference

def __getConnection(db_url, domain=""):
    return MongoClient(db_url).get_database(domain, read_preference=ReadPreference.SECONDARY_PREFERRED)

def find(query, db_url, domain, collection):
    print("Connecting MongoDB for the collection to find the data")
    return list(__getConnection(db_url, domain)[collection].find(query))