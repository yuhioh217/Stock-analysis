from ConfigLoader import ConfigLoader


class CategoryConfigLoader(ConfigLoader):
	"""docstring for CategoryConfigLoader"""
	path = "./config/industry_config.txt"

	def standby_config(self):
		self.setPath(self.path)
		self.load_config()

	def load_category_str(self):
		self.standby_config()
		return self.get_config('url-config','categoryStr')

	def load_mongo_info(self):
		self.standby_config()
		mongo      = self.get_config('url-config','mongoURL')
		db         = self.get_config('url-config','db')
		collection = self.get_config('url-config','collection')
		return {'url':mongo, 'db':db, 'collection':collection}


	def category_array(self):
		category_str = self.load_category_str()
		category_arr = category_str.split(';')
		categoryArr   = []
		for c_str in category_arr:
			category = c_str.split('~')[0]
			category_id = (category.split(' '))[0]
			category_name = (category.split(' '))[1]
			#category_IdArr.append(category_id)
			#category_NameArr.append(category_name)
			itemArr = []
			item = (c_str.split('~'))[1]
			item_each = item.split(',')
			for i_str in item_each:
				item_id = (i_str.split(' '))[0]
				item_name = (i_str.split(' '))[1]
				itemArr.append({'item_id':item_id, 'item_name':item_name})

			categoryArr.append({'category_id':category_id, 'category_name':category_name , 'item':itemArr})
		return categoryArr
