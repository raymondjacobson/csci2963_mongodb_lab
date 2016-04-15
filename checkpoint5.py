import pymongo
import datetime
import random
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
conn=MongoClient()
db = conn.csci2963
definitions = db.definitions

def random_word_requester():
    #find a random record and print out the contents
    collectionCount = db.definitions.count()
    rand = random.randint(0,collectionCount)
    randomRecord = db.definitions.find().limit(1).skip(rand).next()
    randid = randomRecord['_id']
    randword = randomRecord['word']
    randdef = randomRecord['definition']
    #

    result = db.definitions.update_one(
        {"word":randword},
        {
            "$set":{
                "Timestamps":[]
            }
        }
    )

    result = db.definitions.update_one(
        {"word":randword},
        {
            "$push":{
                "Timestamps":str(datetime.datetime.now())
            }
        }
    )


    result = db.definitions.update_one(
        {"word":randword},
        {
            "$push":{
                "Timestamps":str(datetime.datetime.today())
            }
        }
    )

    updatedrecord = db.definitions.find_one({"word":randword})
    print randomRecord['word'] + ": " + randomRecord['definition']
    print updatedrecord['Timestamps']
    #update the contents
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    return


if __name__ == '__main__':
    print random_word_requester()
