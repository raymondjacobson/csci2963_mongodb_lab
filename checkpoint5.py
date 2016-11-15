import random
from time import strftime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.csci2963
collection = db.definitions


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    records = []
    for i in collection.find():
	records.append(i)
    
    c = random.choice(records)
    t = strftime("%Y-%m-%d %H:%M:%S")
    if c.has_key("dates"):
        dates = c.dates
    else:
        dates = []
    dates.append(t)
    collection.update({"_id": c["_id"]}, {"$set": {"dates": t}})

    return c


if __name__ == '__main__':
    print random_word_requester()
