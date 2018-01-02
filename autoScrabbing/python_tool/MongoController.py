from pymongo import MongoClient

class MongoController():
	def __init__(self, options):

		print options['url']

		self.url = options['url'] 
		self.mongo = MongoClient(self.url)
		self.db  = self.mongo[options['db']]
		self.collection = self.db[options['collection']]

		
	def insertData(data):
		try:
			#post_id = (self.collection).insert_one(data).inserted_id
			print data
		except Exception as err:
			print err


