# -*- coding: utf-8 -*- 
import Crawler
import MongoController
import Industry
import time

class StockInfo():
	def __init__(self):
		self.x = ""

	def read_file(self, filePath):
		f = open(filePath, 'r')
		self.stockArr = f.readlines()

	def get_allinfo(self):

		options={
			'url':'mongodb://localhost:27017/',
			'db':'industry',
			'collection':'stock',
		}
		mongo = MongoController.MongoController(options);

		v = Industry.Industry()
		for stock in self.stockArr:
			stock = str(stock).replace("\n","")
			v.getData(stock)
		a = v.returnData()[0]
		print a
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
			print "stock id : " + tempId
			print "date : " + tempDate
			print "end : " + str(tempEnd)

			isEmpty = mongo.findAll({
				"stockId":tempId
			}).count()

			if isEmpty is 0:
				mongo.insertData({
					"stockId":tempId,
					'name' : tempName,
					"data":[
						{
							'date' : tempDate,
							'open' : tempOpen,
							'high' : tempHigh,
							'low'  : tempLow,
							'end'  : tempEnd,
							'yes'  : tempYes,
							'volume': tempVolume,
							'UDVal': tempUDVal,
							'UDRate':tempUDRate
						}
					]
				})

			isRepeat = mongo.findAll({
				"stockId":tempId,
				"data":{"$elemMatch" : {"date":tempDate}}
			}).count()

			if isRepeat is 0:
				mongo.updateData(
					{"stockId":tempId},
					{"$push":{"data":{
						'date' : tempDate,
						'open' : tempOpen,
						'high' : tempHigh,
						'low'  : tempLow,
						'end'  : tempEnd,
						'yes'  : tempYes,
						'volume': tempVolume,
						'UDVal': tempUDVal,
						'UDRate':tempUDRate
					}}}
				)

			time.sleep(0.3)