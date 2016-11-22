from pymongo import MongoClient
client = MongoClient()
from bson.objectid import ObjectId

if __name__ == '__main__':
	db = client.csci2963
	defs = db.definitions

	for definition in defs.find():
		print definition

	print defs.find_one()

	print defs.find({"word": "Word"})

	print defs.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b8b7')})

	defs.insert_one({"word": "NotAWord", "definition": "NotADefinition"})
