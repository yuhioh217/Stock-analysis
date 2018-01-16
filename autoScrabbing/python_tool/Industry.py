# -*- coding: utf-8 -*-  
import os
import json
import time
import requests
import urllib2
import sys
from datetime import date

'''
catch each stock detail information
'''
class Industry():
		def __init__(self):
			self.stockid = []	#Stock id
			self.name = []		#Stock chinese name
			self.dateArr = []	#date
			self.openArr = []	#open value
			self.highArr = []	#high value
			self.lowArr = []	#low value
			self.endArr = []	#end value
			self.yesArr = []	#yesterday end value
			self.volume = []	#stock transaction volume
			self.updownvalue = []#up or down value
			self.updownrate = []#up or down rate

		def getData(self, stock_id):
			data = ""
			req = ""
			tries = 18
			base_url = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?'

			for i in range(tries):
				try:			
					stockId = 'tse_{}.tw'.format(stock_id)#tse
					time_stamp = int(time.time() * 1000 + 1000000)
					self.query_url = '{}ex_ch={}&_={}'.format(base_url, stockId, time_stamp)
					req = requests.session()
					req.get('http://mis.twse.com.tw/stock/index.jsp',headers={'Accept-Language': 'zh-TW'})		
					response = req.get(self.query_url)
					data = json.loads(response.text)
					count = len(data['msgArray'])
					if count == 0:
						stockId = 'otc_{}.tw'.format(stock_id)#otc
						self.query_url = '{}ex_ch={}&_={}'.format(base_url, stockId, time_stamp)
						req.get('http://mis.twse.com.tw/stock/index.jsp',headers={'Accept-Language': 'zh-TW'})		
						response = req.get(self.query_url)
						data = json.loads(response.text)
						count = len(data['msgArray'])
				except Exception as err:
					print "Data : " + str(data)
					print err
					print "Retry " + str(i) + " times"
					req.close()
					time.sleep(10)
					if i < tries - 1: # i is zero indexed
						data = []
						continue
					else:
						raise
				break

			count = len(data['msgArray'])
			#print "count : " + str(count)
			for index in range(0, count):
				print stock_id
				self.stockid.append(stock_id)
				self.name.append(data['msgArray'][index]['n'])		
				openVal  = float(data['msgArray'][index]['o'])
				highVal  = float(data['msgArray'][index]['h'])
				lowVal   = float(data['msgArray'][index]['l'])
				endVal   = float(data['msgArray'][index]['z'])
				yesVal   = float(data['msgArray'][index]['y'])
				volumeVal= float(data['msgArray'][index]['v'])
				self.dateArr.append(data['msgArray'][index]['d'])
				self.openArr.append(openVal)
				self.highArr.append(highVal)
				self.lowArr.append(lowVal)
				self.endArr.append(endVal)
				self.yesArr.append(yesVal)
				self.volume.append(volumeVal)
				self.updownvalue.append(format((endVal-yesVal), '.2f'))
				rateVal = format(((endVal-yesVal)/yesVal)*100, '.2f')
				self.updownrate.append(rateVal)
				time.sleep(0.5)
			'''
			for index in range(0, len(self.name)):
				print "============================"
				print str(self.stockid[index]) + ' ' + self.name[index] 
				print u'開盤:' + str(self.openArr[index])
				print u'收盤:' + str(self.endArr[index])
				print u'昨收:' + str(self.yesArr[index])
				print u'今量:' + str(self.volume[index])
			#print self.volume
			'''


		def returnData(self):
			return [self.stockid, self.name, self.dateArr, self.openArr, self.highArr, self.lowArr, self.endArr, self.yesArr, self.volume, self.updownvalue, self.updownrate]


