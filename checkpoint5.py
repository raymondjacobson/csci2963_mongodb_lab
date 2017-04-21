from pymongo import MongoClient
import random
import datetime
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client.csci2963
    definitions = db.definitions
    column_size = db.command('collStats', 'definitions')['count']
    rand_int = random.randrange(0, column_size-1)
    item = definitions.find_one({"word" : "Ack"})

    if 'dates' not in item.keys():
        item['dates'] = [str(datetime.datetime.now())]
    else:
        item['dates'].append(str(datetime.datetime.now()))

    definitions.update_one({'word' : item['word']}, {'$set' : {'dates' : item['dates']}})

    print definitions.find_one({'word' : item['word']})

    

    
    return item['word'] + item['definition']


if __name__ == '__main__':
    print random_word_requester()
