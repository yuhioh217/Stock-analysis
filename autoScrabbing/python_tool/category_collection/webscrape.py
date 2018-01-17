#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import cfg_loader
'''
init -> setpage -> find tag -> get tag info
'''
class Scrape(object):
	"""docstring for Scrape"""
	def __init__(self):
		super(Scrape, self).__init__()
		self.webpage = webdriver.PhantomJS(executable_path='../bin/phantomjs')
		self.pageURL = ""
		self.soup    = ""

	def setpage(self, itemId):
		c = cfg_loader.ConfigLoader("./industry_config.txt")	#set config init
		self.pageURL = c.getData("url-config", "itemURL")	#get the itemURL field from config
		all_url = '{}a={}'.format(self.pageURL, itemId)
		#print all_url
		self.webpage.get(all_url)
		self.soup = BeautifulSoup(self.webpage.page_source, 'html.parser')

	def getpage(self):
		return self.soup

	def find_all(self, *tags):
		#print "tags size : " + str(len(tags))
		#print self.soup
		return self.soup.find_all(*tags)




		