import ConfigParser

class ConfigLoader(object):
	"""docstring for ConfigLoader"""
	path = None
	
	def __init__(self):
		super(ConfigLoader, self).__init__()
		self.configParser = ""

	def setPath(self, path):
		self.path = path

	def getPath(self):
		return self.path

	def load_config(self):
		self.configParser = ConfigParser.RawConfigParser()
		self.configParser.read(self.path)

	def get_config(self, cfg_session, cfg_option):
		return self.configParser.get(cfg_session, cfg_option)

