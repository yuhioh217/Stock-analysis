from lib.MongoDatabase.MongoController import MongoController

class DataBase(object):
	"""docstring for DataBase"""
	m_options = None
	'''
		m_options = {
			'url':'mongodb://localhost:27017/',
			'db':'industry',
			'collection':'stock'
		}
	'''
	def __init__(self):
		super(DataBase, self).__init__()
		self.db = self.db_connection()
		self.stockId = ""
		self.date = ""

	def db_connection(self):
		if self.m_options is None:
			return ""
		return  MongoController(self.m_options)

	


		