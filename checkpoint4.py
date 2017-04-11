from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()

if __name__ == '__main__':
    db = client.csci2963
    defs = db.definitions

    print "\nFind all records:"
    for x in defs.find({}):
        print x

    print "\nFind one record:"
    print defs.find_one()

    print "\nFind a specific record:"
    print defs.find_one({"word": "Capitaland"})

    print "\nFind a specific record:"
    print defs.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b949')})

    print "\nInsert a record:"
    defs.insert({"word": "foo", "definition": "bar"})
    print defs.find_one({"word": "foo"})
