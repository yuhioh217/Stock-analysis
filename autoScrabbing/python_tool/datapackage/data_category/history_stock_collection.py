# -*- coding: utf-8 -*-
from lib.StockLoader.stockhistorythread import StockHistroyParser
from lib.StockIdLoader.StockIdParser import StockIdParser
from Queue import Queue
from threading import Thread


def main():
	url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY'
	cookie = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY'

	u_stock = StockIdParser()
	u_stock.read_file('config/center.txt')
	u_stock_center = u_stock.get_Stock()

	for stock in u_stock_center:
		print stock
		task = StockHistroyParser(url, cookie, stock)
		task.data_record()


if __name__ == '__main__':
	main()