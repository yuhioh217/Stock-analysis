from pymongo import MongoClient

class MongoController():
	def __init__(self, options):

		print options['url']

		self.url = options['url'] 
		self.mongo = MongoClient(self.url)
		self.db  = self.mongo[options['db']]
		self.collection = self.db[options['collection']]

		
	def insertData(self, data):
		try:

			post_id = (self.collection).insert_one(data).inserted_id
		except Exception as err:
			print err


