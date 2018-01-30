import requests
import time
from lib.MongoDatabase.MongoController import MongoController
from lib.ConfigLoader.CategoryConfigLoader import CategoryConfigLoader

class StockHistroyParser():

	def __init__(self, url, cookie, stockId):
		self.active = False
		self.url    = url
		self.cookie = cookie
		self.stockId= stockId
		self.session = self.fetch_cookies()
		self.db = ""

	def query_json(self,headers, query_str):
		try:
			response = self.session.request("GET", self.url, headers=headers, params=query_str)
			if response.json().get('data') is None or response.json().get('data') == "   " or response.json().get('stat') != "OK":
				print "cookie expire"
				self.update_session()
				response = self.session.request("GET", self.url, headers=headers, params=query_str)
			return response.json()['data']
		except Exception as err:
			print "[ stockhistorythread.py : Line 25]"
			time.sleep(5)
			print err
			return ""

	def fetch_cookies(self):
		_session = requests.session()
		_session.get(self.cookie)
		return _session

	def update_session(self):
		r = (self.session).get(self.cookie)
		if r.cookies.get_dict():
			(self.session).cookies.update(r.cookie)

	def date_arr(self):
		arr = []
		for y in range(2015,2019):
			if y == 2018:
				for n in range(1,2):
					if n < 10:
						arr.append(str(y)+'0'+str(n)+'01')
					else:
						arr.append(str(y)+str(n)+'01')
			else:
				for m in range(1,13):
					if m < 10:
						arr.append(str(y)+'0'+str(m)+'01')
					else:
						arr.append(str(y)+str(m)+'01')
		print arr
		return arr

	def data_record(self):
		if self.db == "":
			config_fetch = CategoryConfigLoader()
			m_options = config_fetch.load_mongo_info()
			self.db = MongoController(m_options)
		self.db.changeCollection('stock')

		for date in self.date_arr(): 
			timestamp = str(int(time.time()*1000))
			query_string = {
				'_':timestamp,
				'stockNo':self.stockId,
				'response':'json',
				'date':date
			}
			headers = {
				'content-type': 'application/json',
			}
			try:
				data = self.query_json(headers, query_string)
				#print data
				for info in data:
					dateTime = info[0].replace('/','')
					volumeVal = float(info[1].replace(',',''))//1000
					try:
						openVal =  float(info[3])
						highVal =  float(info[4])
						lowVal  =  float(info[5])
						endVal  =  float(info[6])
						try:
							updownVal = float(info[7])
						except Exception as err:
							updownVal = 0

						yesVal  = float(info[6]) - updownVal
						updownrate  = format(((endVal-yesVal)/yesVal)*100, '.2f')
					except Exception as err:
						openVal = 0
						highVal = 0
						lowVal  = 0
						endVal  = 0
						updownVal = 0
						yesVal = 0
						updownrate = 0

					print dateTime
					print 'yesVal :' + str(yesVal)
					print 'endVal :' + str(endVal)
					print 'updownVal :' + str(updownVal)
					print 'updownrate :' + str(updownrate)

					isRepeat = self.db.findAll({
						"stockId":self.stockId,
						"data":{"$elemMatch" : {"date":dateTime}}
					}).count()
					if isRepeat is 0:
						self.db.updateData(
							{"stockId":self.stockId},
							{"$push":{"data":{
								'date' : dateTime,
								'open' : openVal,
								'high' : highVal,
								'low'  : lowVal,
								'end'  : endVal,
								'yes'  : yesVal,
								'volume': volumeVal,
								'UDVal': updownVal,
								'UDRate':updownrate
							}}}
						)
				time.sleep(3)
			except Exception as err:
				print err
				time.sleep(3)


