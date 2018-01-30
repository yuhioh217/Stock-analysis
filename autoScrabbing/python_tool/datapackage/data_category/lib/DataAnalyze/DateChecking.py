from DataBase import DataBase

class DateChecking(DataBase):
	"""docstring for DateChecking"""
	m_options = {
		'url':'mongodb://localhost:27017/',
		'db':'industry',
		'collection':'stock'
	}

	def lock_stock(self, stockId):
		self.stockId = stockId

	def include_data_by_date(self, date): #date format should be "20070101"
		
		dateFormatArr = []
		dateFormatArr.append(date)
		if len(date) == 8:
			dateFormatArr.append(str(int(date[0:4])-1911) + date[4:6] + date[6:8])
		elif len(date) == 6:
			dateFormatArr.append(str(int(date[0:2])+1911) + date[2:4] + date[4:6])

		print dateFormatArr
		for date in dateFormatArr:
			isExist = self.db.findAll(
				{
					'stockId':self.stockId
				},{
					'data':{
						'$elemMatch': {
							'date':date
						}
					}
				}
			).count()
			print isExist
			if isExist > 0:
				self.date = date
				return True
		return False


	def fetch_data(self, field): #before doing fetch_data, you should use "include_data_by_date to check data exist or not."
		try:
			data = self.db.findAll(
				{
					'stockId':self.stockId
				},{
					'data':{
						'$elemMatch': {
							'date':self.date
						}
					}
				}
			)
			print data
			return data[0]['data'][0][field] #One field should be one data in one day
		except Exception as err:
			print err
			return ""



