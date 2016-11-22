from pymongo import MongoClient
client = MongoClient()


def random_word_requester():
	'''
	This function should return a random word and its definition and also
	log in the MongoDB database the timestamp that it was accessed.
	'''
	client = MongoClientclient = MongoClient('localhost', 27017)
	db = client.csci2963
	db.authenticate("admin", "admin123", "admin")
	collection = db.definitions


	collection.aggregate([{ $sample: { size: 1 } }])
	return


if __name__ == '__main__':
	print random_word_requester()
