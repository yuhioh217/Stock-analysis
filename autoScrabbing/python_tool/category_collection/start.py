#!/usr/bin/python
# -*- coding: utf-8 -*-
import cfg_loader
import db_connection
import sys
import webscrape
import re
import time

sys.path.append('../')
import MongoController


if __name__ == '__main__':
	
	db  = db_connection.DB()
	db.connect()
	print db.getDB()
	scrape = webscrape.Scrape()
	'''
		Process category string
	'''
	in_cfg = cfg_loader.ConfigLoader('./industry_config.txt')
	industryStr = in_cfg.getData('url-config','categoryStr')
	industryArr = industryStr.split(';')
	categoryIdArr = []
	categoryNameArr = []

	db.createCollection("all")#all collection is used to save category info
	#=====================================#
	for index in range(0,len(industryArr)):
		print "===="
		category = (industryArr[index].split('~'))[0]
		category_id = (category.split(' '))[0]
		category_name = (category.split(' '))[1]
		print "=============="
		print "category_name : " + category_name
		print "category_id : " + category_id
		categoryIdArr.append(category_id)
		categoryNameArr.append(category_name)
		db.createCollection(category_id)

		item = (industryArr[index].split('~'))[1]
		item_each = item.split(',')

		for item_index in range(0,len(item_each)):
			item_id = (item_each[item_index].split(' '))[0]
			item_name = (item_each[item_index].split(' '))[1]
			print item_name
			print item_id
			db.changeCollection(category_id)
			db.insertData({
				"itemId"   : item_id,
				"itemName" : item_name
			})
			scrape.setpage(item_id)
			stock_td_tag = scrape.find_all('td','t3t1')
			stock_td_tag_rev = scrape.find_all('td','t3t1_rev')
			exist_bool = db.createCollection(item_id)
			#print exist_bool
			if(exist_bool is True):
				
				db.changeCollection(item_id)

				for td in stock_td_tag:
					a_str = (td.find('a')).text
					stock_id = re.match('\d+\w?',a_str).group(0)
					stock_name = re.sub(stock_id+"\s*", "", a_str)
					db.insertData({
										"stockId"   : stock_id,
										"stockName" : stock_name
									});
					print stock_id
					print stock_name

				for td in stock_td_tag_rev:
					a_str = (td.find('a')).text
					stock_id = re.match('\d+\w?',a_str).group(0)
					stock_name = re.sub(stock_id+"\s*", "", a_str)
					db.insertData({
										"stockId"   : stock_id,
										"stockName" : stock_name
									});
					print stock_id
					print stock_name
		time.sleep(1)


	db.changeCollection("all")
	for index in range(0,len(categoryIdArr)):
		db.insertData({
			"categoryId"   : categoryIdArr[index],
			"categoryName" : categoryNameArr[index]
		});
	print categoryIdArr
	print categoryNameArr