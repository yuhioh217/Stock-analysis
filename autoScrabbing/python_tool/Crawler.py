import os
import json
import time
import requests
import urllib2
from datetime import date

class Crawler():
		def __init__(self, dateStr):
			self.dateArr = []
			self.dataArr = []
			
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
			for index in range(0, count-1):
				self.dateArr.append(data['data'][index][0])
				self.dataArr.append(data['data'][index][4])
				
			return [self.dateArr, self.dataArr]