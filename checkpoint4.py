from pymongo import MongoClient

if __name__ == '__main__':
	from bson.objectid import ObjectId

	client = MongoClientclient = MongoClient('localhost', 27017)
	db = client.csci2963
	db.authenticate("admin", "admin123", "admin")
	collection = db.definitions

	print collection.find_one()

	for post in collection.find():
		print post

	print collection.find_one({"word": "hello"})
	print collection.find_one({"_id": ObjectId('582ecdf52c178ef676e9e5ff')})
	print collection.find_one({"_id": ObjectId(str(collection.insert({"word": "goodbye", "definition": "exclam. used to express good wishes when parting or at the end of a conversation."})))})