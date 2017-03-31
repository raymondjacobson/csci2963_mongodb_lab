import pymongo
from pymongo import MongoClient
import pprint


client = MongoClient()

db = client['csci2963']

coll = db.defintions

if __name__ == '__main__':
    #Fetch all records
    pprint.pprint(coll.find())
    #Fetch one record
    pprint.pprint(coll.find_one())
    #Fetch a specific record
    pprint.pprint(coll.find_one({"word":"Capitaland"}))
    #Fetch a record by object id
    pprint.pprint(coll.find_one({"_id": 'ObjectId("56fe9e22bad6b23cde07b8ce")'}))
    #Insert a new record
    word = {"word": "T430s",
        "definition" : "The model of computers used after T430. Is it as good?"}
    insert_id = coll.insert_one(word).inserted_id
    insert_id

