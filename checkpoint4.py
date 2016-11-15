from pymongo import MongoClient
client = MongoClient()

if __name__ == '__main__':
	client = MongoClient('localhost', 27017)
	db = client.csci2963
	collection = db.definitions
	# fetch all records
	print 'all records:'
	for i in collection.find():
		print i
	# fetch one record
	print 'one record:', collection.find_one()
	# fetch a specific record
	print 'specific record:', collection.find({"word": "Foo"})
	# fetch a record by object id
	print 'record by object id:', collection.find({"_id": "56fe9e22bad6b23cde07b8ce"})
	# insert a new record
	collection.insert({"word": "definition"})
