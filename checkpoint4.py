from pymongo import MongoClient
import pprint
client = MongoClient()

if __name__ == '__main__':
    client = MongoClient()
    db = client.csci2963
    definitions = db.definitions
    whole_thing = definitions.find()

    #going to try and insert a new word

    new_thing = {"word" : "Resident Assistant",
                 "definition" : "n. Someone who makes sure you're OK if you live on-campus. "
                 }

    new_thing_id = definitions.insert_one(new_thing).inserted_id

    
    for thing in whole_thing:
        pprint.pprint(thing)

    print "\nJust one record\n"

    pprint.pprint(definitions.find_one())

    print "\nJust one specific record, Memes.\n"

    
    pprint.pprint(definitions.find_one({"word" : "Memes"}))


    print "\n Trying to find a record by object id\n"


    pprint.pprint(definitions.find_one({"_id": new_thing_id}))

    
