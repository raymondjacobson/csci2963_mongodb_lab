import random
import time
from pymongo import MongoClient
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client.csci2963
    defs = db.definitions
    allwords = [x["word"] for x in defs.find({})]
    word = random.choice(allwords)
    defs.update({"word": word}, {"$push": {"dates": time.asctime(time.localtime())}})
    return defs.find_one({"word": word})


if __name__ == '__main__':
    print random_word_requester()
