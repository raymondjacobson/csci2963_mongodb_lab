from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('localhost',25565)

if __name__ == '__main__':
    db = client['csci2963']
    defs = db['definitions']

    #Fetch all records
    print 'Fetching all records'
    for definition in defs.find():
        print definition
    
    #Fetch one record
    print 'Fetching first record'
    print defs.find_one()
    
    #Fetch specific record
    print 'Fetching Capitaland'
    print defs.find_one({'word':'Capitaland'})
    
    #Fetch by object id
    print 'Fetching by ObjectId'
    print defs.find_one({'_id':ObjectId('56fe9e22bad6b23cde07b8ce')})

    #Insert a new object
    print 'Inserting dog'
    defs.insert_one({'word':'dog','definition':"n. Man's best friend"})
    print defs.find_one({'word':'dog'})
