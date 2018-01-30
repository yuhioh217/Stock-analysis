# -*- coding: utf-8 -*- 
import sys
import time

class StockIdParser(object):
	def __init__(self):
		self.x = ""

	def read_file(self, filePath):
		f = open(filePath, 'r')
		self.stockArr = f.readlines()

	def get_Stock(self):
		self.stockArr = [stock.replace('\n','') for stock in self.stockArr]
		if len(self.stockArr) is 0:
			return "No data in it"
		return self.stockArr