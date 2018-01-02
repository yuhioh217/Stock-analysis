import sys
sys.path.append('./Crawler.py')
sys.path.append('./MongoController.py')
import Crawler
import MongoController

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
			data = Crawler.Crawler(date_str)
			dateArr = data.getData()[0]
			dataArr = data.getData()[1]
			print dateArr
			#print 'Prepare to insert data to mongoDB'