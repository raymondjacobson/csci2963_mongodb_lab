import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
# Connection to Mongo DB
try:
    conn=MongoClient()
    db = conn.csci2963
    definitions = db.definitions

    print "Printing all entries in the database!"
    for d in definitions.find():
        print d


    print "Printing the first element in the database!"
    print definitions.find_one()


    print "fetching a specific item"
    print definitions.find_one({"word": "Love Canal"})


    print "fetching a specific item by _id"
    print definitions.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")})


    print "Insert a new word into the database"
    post = {"word" : "Hecht","definition" : "One who eat's many eggs"}
    post_id = definitions.insert_one(post).inserted_id
    print post_id


except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn
