# -*- coding: utf-8 -*-  
import sys
sys.path.append('./Crawler.py')
sys.path.append('./MongoController.py')
sys.path.append('./Industry.py')
import Crawler
import MongoController
import Industry
import time

if __name__ == '__main__':


	'''
	#大盤
	options={
		'url':'mongodb://localhost:27017/',
		'db':'stock',
		'collection':'market',
	}
	mongo = MongoController.MongoController(options);
	for year in range(20018,2019):
		for month in range(2,3):
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
	'''
	#產業 分類
	options={
		'url':'mongodb://localhost:27017/',
		'db':'industry',
		'collection':'cement',
	}
	mongo = MongoController.MongoController(options);
	cement_id = [1101,1102,1103,1104,1108,1109,1110]	#水泥
	v = Industry.Industry()
	for id in cement_id:
		#print id
		v.getData(id)
	a = v.returnData()[0]
	print len(a)
	for index in range(0, len(a)):
		tempId = v.returnData()[0][index]
		tempName = (v.returnData()[1][index]).encode('utf8')
		tempDate = v.returnData()[2][index]
		tempOpen = v.returnData()[3][index]
		tempHigh = v.returnData()[4][index]
		tempLow = v.returnData()[5][index]
		tempEnd = v.returnData()[6][index]
		tempYes = v.returnData()[7][index]
		tempVolume = v.returnData()[8][index]
		tempUDVal = v.returnData()[9][index]
		tempUDRate = v.returnData()[10][index]

		mongo.insertData({
			'stockid' : tempId,
			'name' : tempName,
			'date' : tempDate,
			'open' : tempOpen,
			'high' : tempHigh,
			'low'  : tempLow,
			'end'  : tempEnd,
			'yes'  : tempYes,
			'volume': tempVolume,
			'UDVal': tempUDVal,
			'UDRate':tempUDRate
		})
	