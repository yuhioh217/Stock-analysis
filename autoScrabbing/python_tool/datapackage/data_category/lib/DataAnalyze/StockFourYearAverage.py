from DataBase import DataBase

class StockFourYearAverage(DataBase):
	"""docstring for StockFourYearAverage"""
	m_options = {
		'url':'mongodb://localhost:27017/',
		'db':'industry',
		'collection':'stock'
	}

	def query_stock_by_date(self,stockId,date):
		return self.db.findAll(
			{
				'stockId':stockId
			},{
				'data':{
					'$elemMatch': {
						'date':date
					}
				}
			}
		)