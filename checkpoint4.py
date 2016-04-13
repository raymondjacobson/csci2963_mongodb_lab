from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['csci2963']
collection = db['definitions']
posts = db.posts

if __name__ == '__main__':
    print posts.find_one()
    print "Modify me"
