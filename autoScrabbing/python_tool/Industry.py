import os
import json
import time
import requests
import urllib2
from datetime import date

class Industry():
		def __init__(self, dateStr):
			self.dateArr = []
			self.openArr = []
			self.highArr = []
			self.lowArr = []
			self.endArr = []
			
			base_url = 'http://www.twse.com.tw/indicesReport/MI_5MINS_HIST?'
			self.query_url = '{}response=json&date={}'.format(base_url, dateStr)
			print 'Process' , self.query_url
		def getData(self):
			try:
				req = requests.get(self.query_url)
				data = json.loads(req.content)

			except Exception as err:
				print err
				data = []
			count = len(data['data'])	
			print count
			for index in range(0, count):
				self.dateArr.append(data['data'][index][0])
				self.openArr.append(data['data'][index][1])
				self.highArr.append(data['data'][index][2])
				self.lowArr.append(data['data'][index][3])
				self.endArr.append(data['data'][index][4])

		def returnData(self):
			return [self.dateArr, self.openArr, self.highArr, self.lowArr, self.endArr]