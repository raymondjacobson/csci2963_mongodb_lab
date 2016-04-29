from pymongo import MongoClient
from random import randint
from bson.objectid import ObjectId
import datetime

client = MongoClient('localhost',25565)
db = client['csci2963']
defs = db['definitions']

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    words = [word for word in defs.find()]
    rnum = randint(0,len(words))
    rword = words[rnum]
    try:
        dates = rword['dates']
    except:
        dates = []
    dates.append(str(datetime.datetime.utcnow()))
    defs.find_one_and_update({'_id':ObjectId(rword['_id'])},{'$set':{'dates':dates}})
    return defs.find_one({'_id':ObjectId(rword['_id'])})


if __name__ == '__main__':
    print random_word_requester()
