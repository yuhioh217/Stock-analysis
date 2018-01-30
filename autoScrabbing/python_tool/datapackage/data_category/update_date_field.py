from lib.MongoDatabase.MongoController import MongoController
from lib.StockIdLoader.StockIdParser import StockIdParser

#update date filed from public year to ROC_year #format => ex. 20180130 => 1070130
if __name__ == '__main__':
	m_options = {
		'url':'mongodb://localhost:27017/',
		'db':'industry',
		'collection':'stock'
	}
	u_stock = StockIdParser()
	u_stock.read_file('config/center.txt')
	u_stock_center = u_stock.get_Stock()
	db = MongoController(m_options)
	
	arr = []
	for y in range(2018,2019):
		if y == 2018:
			for n in range(1,2):
				if n < 10:
					mon = '0'+str(n)
				else:
					mon = str(n)

				for d in range(25,32):		
					if d < 10:		
						arr.append(str(y)+ mon +'0'+str(d))
					else:
						arr.append(str(y)+ mon + str(d))

		else:
			for n in range(1,13):
				if n < 10:
					mon = '0'+str(n)
				else:
					mon = str(n)

				for d in range(25,32):		
					if d < 10:	
						arr.append(str(y)+ mon +'0'+str(d))
					else:
						arr.append(str(y)+ mon + str(d))
	print arr

	for stock in u_stock_center:
		for a in arr:
			roc_date = str(int(a[0:4])-1911) + a[4:6] + a[6:8]
			data = db.updateData(
				{
					'stockId':stock,
					'data':{
						'$elemMatch': {
							'date':a
						}
					}
				},
				{
					'$set':{
						'data.$.date':roc_date
					}
				}
			)

