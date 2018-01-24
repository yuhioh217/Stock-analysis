# -*- coding: utf-8 -*-

from lib.FetchPageData.CategoryDataFetch import CategoryDataFetch
from lib.ConfigLoader.CategoryConfigLoader import CategoryConfigLoader
from lib.MongoDatabase.MongoController import MongoController
from selenium import webdriver
import time
import json
import re

if __name__ == '__main__':
	#set phantomJS to driver
	driver = webdriver.PhantomJS(executable_path='./bin/phantomjs')
	
	#category str process
	config_fetch = CategoryConfigLoader()
	c_arr     = config_fetch.category_array()
	m_options = config_fetch.load_mongo_info()
	print m_options
	#connect to mongoDB
	db = MongoController(m_options)
	db.createCollection("all")

	for c_each_json in c_arr:
		c_each_json_str = json.dumps(c_each_json)
		c_json          = json.loads(c_each_json_str)
		c_id            = c_json['category_id']
		c_name          = c_json['category_name']

		db.changeCollection("all")
		db.insertData({
			"categoryId"   : c_id,
			"categoryName" : c_name
		})

		db.createCollection(c_id)
		
		for item in c_json['item']:
			
			db.changeCollection(c_id)
			item_id = item['item_id']
			item_name = item['item_name']
			db.insertData({
				"itemId"   : item_id,
				"itemName" : item_name
			})
			category_fetch = CategoryDataFetch(driver)
			category_fetch.set_page(item['item_id'])
			stock_list = category_fetch.get_stock_info()

			_exist = db.createCollection(item_id)
			db.changeCollection(item_id)

			for stock in stock_list:
				stock_id = re.match('\d+\w?',stock).group(0)
				stock_name = re.sub(stock_id+"\s*", "", stock)
				print stock_id + " " + stock_name

				if _exist is True:
					db.insertData({
						"stockId"   : stock_id,
						"stockName" : stock_name
					});
		time.sleep(1)