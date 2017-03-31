from pymongo import MongoClient
import random
import datetime
import pprint

client = MongoClient()
db = client.csci2963
coll = db.definitions

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    count = coll.count()
    doc = coll.find()[random.randrange(count)]
    #doc = coll.aggregate([ {$sample: {size:1} } ])
    doc['word']+ " : " +doc['definition']
    return [ doc['word'], doc['definition'] ]


if __name__ == '__main__':
    word_def = random_word_requester()
    print(word_def)
    coll.update_one( {'word':word_def[0]}, { '$push': { 'dates': datetime.datetime.utcnow() } } )
    pprint.pprint( coll.find_one( {'word':word_def[0]} ) )
