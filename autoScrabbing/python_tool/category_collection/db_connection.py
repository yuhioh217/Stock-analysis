import cfg_loader
import sys
sys.path.append('../')
import MongoController

class DB(object):
	"""docstring for DBConnection"""
	def __init__(self):
		super(DB, self).__init__()
		self.config = cfg_loader.ConfigLoader("./industry_config.txt")
		self.mongo = ""
		self.db = ""
		self.collection = ""
		self.mongoDB =""

	def chgconfig(self,cfgPath):
		self.config = cfg_loader.ConfigLoader(cfgPath)
		if self.mongoDB != "":
			self.mongoDB.close()
			print "Reset the mongoDB info, reconnection DB."
			self.connect()

	def connect(self):
		self.mongo = self.config.getData("url-config", "mongoURL")
		self.db = self.config.getData("url-config", "db")
		self.collection = self.config.getData("url-config", "collection")
		options = {
			'url' : self.mongo,
			'db' : self.db,
			'collection' : self.collection
		}
		self.mongoDB = MongoController.MongoController(options)

	def getDB(self):
		if self.mongoDB == "":
			print "MongoDB doesn't set!!"
			return 0
		else:
			return self.mongoDB

	def createCollection(self, name):
		return (self.mongoDB).createCollection(name)

	def changeCollection(self, name):
		(self.mongoDB).changeCollection(name)

	def insertData(self, data):
		(self.mongoDB).insertData(data)