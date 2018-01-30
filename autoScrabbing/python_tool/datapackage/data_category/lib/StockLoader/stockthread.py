from threading import Thread
from lib.MongoDatabase.MongoController import MongoController
from lib.ConfigLoader.CategoryConfigLoader import CategoryConfigLoader
import requests
import time

class StockParser(Thread):
	"""docstring for JSONBase"""
	'''
		url : http://mis.twse.com.tw/stock/api/getStockInfo.jsp
		cookies : http://mis.twse.com.tw/stock/fibest.jsp?lang=zh_tw (enter webpage)
	'''
	def __init__(self, url, cookie, stock_arr, flag):
		#flag is 0 ==> center, flag is 1 ==> cabinet
		Thread.__init__(self)
		print "Fetching cookies from " + url
		self.active = False
		self.url = url
		self.cookie = cookie
		self.stock_arr = stock_arr
		self.flag = flag
		self.session = self.fetch_cookies()
		self.stock_str = self.quer_str()
		self.db = ""
	
	def quer_str(self):
		if self.flag is 0:
			stockId = '%7c'.join('tse_{}.tw'.format(stock_id) for stock_id in self.stock_arr)
		else:
			stockId = '%7c'.join('otc_{}.tw'.format(stock_id) for stock_id in self.stock_arr)
		return stockId

	def query_json(self, headers, query_str):
		try:
			response = self.session.request("GET", self.url, headers=headers, params=query_str)
			if response.json().get('msgArray') is None or response.json().get('msgArray') == "   ":
				print "cookie expire"
				self.update_session()
				response = self.session.request("GET", self.url, headers=headers, params=query_str)
			return response.json()['msgArray']
		except Exception as err:
			print "[ JSONBase.py Err : Line 19 ]"
			print err

	def fetch_stock_info(self, jsonArr):
		
		for json in jsonArr:
			data = self.condition(json)
			print data
			self.data_record(data)
			time.sleep(0.5)

	def condition(self, json):
		try:
			if json['o'].encode('utf-8') == '-':
				# no transaction today
				stockId  = json['c']
				dateTime = json['d']
				stockName= json['n']
				openVal  = float(json['y'])
				highVal  = float(json['y'])
				lowVal   = float(json['y'])
				endVal   = float(json['y'])
				yesVal   = float(json['y'])
				volumeVal= 0
				updownvalue = 0
				updownrate = 0
			else:
				stockId  = json['c']
				dateTime  = json['d']
				stockName= json['n']
				openVal  = float(json['o'])
				highVal  = float(json['h'])
				lowVal   = float(json['l'])
				endVal   = float(json['z'])
				yesVal   = float(json['y'])
				volumeVal= float(json['v'])
				updownvalue = format((endVal-yesVal), '.2f')
				updownrate  = format(((endVal-yesVal)/yesVal)*100, '.2f')
		except Exception as err:
			# no transaction today
			stockId  = json['c']
			stockName= json['n']
			dateTime = json['d']
			openVal  = float(json['y'])
			highVal  = float(json['y'])
			lowVal   = float(json['y'])
			endVal   = float(json['y'])
			yesVal   = float(json['y'])
			volumeVal= 0
			updownvalue = 0
			updownrate = 0
		return {'stockId':stockId,'stockName':stockName,'dateTime':dateTime, 'open':openVal, 'high':highVal, 'low':lowVal, 'end':endVal, 'yes':yesVal, 'vol':volumeVal, 'updownvalue':updownvalue, 'updownrate':updownrate}


	def data_record(self, data):
		if self.db == "":
			config_fetch = CategoryConfigLoader()
			m_options = config_fetch.load_mongo_info()
			self.db = MongoController(m_options)
		self.db.changeCollection('stock')
		date = data['dateTime']
		roc_date = str(int(date[0:4])-1911) + date[4:6] + date[6:8]

		isEmpty = self.db.findAll({
			"stockId":data['stockId']
		}).count()

		if isEmpty is 0:
			self.db.insertData({
				"stockId":data['stockId'],
				'name' : data['stockName'],
				"data":[
					{
						'date' : roc_date,
						'open' : data['open'],
						'high' : data['high'],
						'low'  : data['low'],
						'end'  : data['end'],
						'yes'  : data['yes'],
						'volume': data['vol'],
						'UDVal': data['updownvalue'],
						'UDRate':data['updownrate']
					}
				]
			})
		isRepeat = self.db.findAll({
			"stockId":data['stockId'],
			"data":{"$elemMatch" : {"date":roc_date}}
		}).count()
		if isRepeat is 0:
			self.db.updateData(
				{"stockId":data['stockId']},
				{"$push":{"data":{
					'date' : roc_date,
					'open' : data['open'],
					'high' : data['high'],
					'low'  : data['low'],
					'end'  : data['end'],
					'yes'  : data['yes'],
					'volume': data['vol'],
					'UDVal': data['updownvalue'],
					'UDRate':data['updownrate']
				}}}
			)



	def fetch_cookies(self):
		_session = requests.session()
		_session.get(self.cookie)
		return _session

	def update_session(self):
		r = (self.session).get(self.cookie)
		if r.cookies.get_dict():
			(self.session).cookies.update(r.cookie)

	def run(self):
		self.active = True

		timestamp = str(int(time.time()*1000))
		query_string = {
			'ex_ch':self.stock_str,
			'json':'1',
			'delay':'0',
			'_':timestamp
		}
		headers = {
			'content-type': 'application/json',
		}
		data = self.query_json(headers, query_string)
		#print data
		self.fetch_stock_info(data)

	def stop(self):
		self.active = False
