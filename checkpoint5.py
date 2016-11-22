from pymongo import MongoClient
client = MongoClient()
import random
import time

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client.csci2963
    defs = db.definitions
    count = defs.count()
    rand_word = defs.find().limit(-1).skip(random.randint(0, count-1))
    for w in rand_word:
    	word = w
   	print 
    defs.update(word, {"$push": {"dates": time.strftime("%Y-%m-%d %H:%M:%S")}})
    return defs.find_one(word)


if __name__ == '__main__':
    print random_word_requester()
