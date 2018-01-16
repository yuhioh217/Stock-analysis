from pymongo import MongoClient

class MongoController():
	def __init__(self, options):

		#print options['url']
		self.url = options['url'] 
		self.mongo = MongoClient(self.url)
		self.db  = self.mongo[options['db']]
		self.collection = self.db[options['collection']]

		
	def insertData(self, data):
		try:
			post_id = (self.collection).insert_one(data).inserted_id
		except Exception as err:
			print err


	def createCollection(self, name):
		try:
			create_text = (self.db).create_collection(name)
			return True
			#print create_text
		except Exception as err:
			print err
			print "Collection already exist---"
			return False
	def changeDB(self, db):
		self.db  = self.mongo[db]

	def changeCollection(self, collection):
		self.collection = self.db[collection]

	def closeDB(self):
		self.mongo.close()

	def findAll(self, query):
		return self.collection.find(query)

	def updateData(self, query, update):
		return self.collection.update(
			query,
			update
		)
		'''
		usage in python:
		mongo.updateData(
			{"stockId":"6116"},
			{"$push":{"data":{"date":"20180114","end":"22.5"}}}
		)
		'''