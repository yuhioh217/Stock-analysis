import ConfigParser

class ConfigLoader(object):
	"""docstring for ConfigLoader"""
	def __init__(self, cfgPath):
		super(ConfigLoader, self).__init__()
		self.path = cfgPath
		self.configParser = ConfigParser.RawConfigParser()
		self.configParser.read(cfgPath)

	def getData(self, cfg_session, cfg_option):
		return self.configParser.get(cfg_session, cfg_option)