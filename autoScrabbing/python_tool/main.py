import sys
sys.path.append('./Crawler.py')
sys.path.append('./MongoController.py')
import Crawler
import MongoController
import time

if __name__ == '__main__':
	
	options={
		'url':'mongodb://localhost:27017/',
		'db':'stock',
		'collection':'market',
	}
	mongo = MongoController.MongoController(options);

	for year in range(2007,2018):
		for month in range(1,13):
			year_str = str(year)
			if month < 10:
				month_str = '0'+ str(month)
			else:
				month_str = str(month)
			date_str = year_str + month_str + '01'
			print date_str
			dataCrawler = Crawler.Crawler(date_str)
			dateGet = dataCrawler.getData()
			data = dataCrawler.returnData()

			for index in range(0,len(data[0])):
				tempDate = data[0][index]
				tempOpen = data[1][index]
				tempHigh = data[2][index]
				tempLow  = data[3][index]
				tempEnd  = data[4][index]
				mongo.insertData({
					'date' : tempDate,
					'open' : tempOpen,
					'high' : tempHigh,
					'low'  : tempLow,
					'end'  : tempEnd
				})
			time.sleep(5)	
			#print 'Prepare to insert data to mongoDB'