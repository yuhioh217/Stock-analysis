# -*- coding: utf-8 -*-  
import Crawler
import MongoController
import Industry
import time


class stock():
	def __init__(self, option):
		self.options= option

	def fetchData(self):
		'''
		產業 分類
		截取產業中各股的開收盤資料
		'''
		mongo = MongoController.MongoController(self.options);
		all_industry = mongo.findAll({})

		cnArr = []	#category name array
	 	ciArr = []	#category id array
		for industry in all_industry:
			print industry['categoryName']
			print industry['categoryId']
			cnArr.append(industry['categoryName'])
			ciArr.append(industry['categoryId'])
		
		#print cnArr[0]
		#print ciArr[0]
		for i_index in range(0, len(ciArr)):
			mongo.changeCollection(ciArr[i_index])
			category_info = mongo.findAll({})
			print "= = = = Industry  = = = ="
			print "   " + cnArr[i_index]
			print "= = = = = = = = = = = = ="
			for category in category_info:
				print "- - - - - - - - - - - - -"
				print "   " + category["itemName"]
				print "- - - - - - - - - - - - -"
				mongo.changeCollection(category["itemId"])
				stock_info = mongo.findAll({})
				snArr = []
				siArr = []

				v = Industry.Industry()
				for stock in stock_info:
					#print "   " + stock["stockId"] + "  " + stock["stockName"]
					siArr.append(stock["stockId"])
					snArr.append(stock["stockName"])
					v.getData(stock["stockId"])
				print siArr
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

					
					mongo.changeDB("industry")
					mongo.changeCollection("stock")




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

					time.sleep(0.2)

		