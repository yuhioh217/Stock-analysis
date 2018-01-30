# -*- coding: utf-8 -*-
from lib.StockIdLoader.StockIdParser import StockIdParser
from lib.StockLoader.stockthread import StockParser

#stock today info

def main():
	url = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp'
	cookies = 'http://mis.twse.com.tw/stock/fibest.jsp?lang=zh_tw'

	u_stock = StockIdParser()
	u_stock.read_file('config/center.txt')
	u_stock_center = u_stock.get_Stock()
	u_stock.read_file('config/cabinet.txt')
	u_stock_cabinet = u_stock.get_Stock()
	u_Arr_cabinet = []
	sum = 0
	u_Arr_center = []
	try:
		for stock in u_stock_center:
			index = u_stock_center.index(stock)
			u_Arr_center.append(stock)
			if (len(u_Arr_center) is len(u_stock_center)/10) or (len(u_Arr_center) > 99) or (index is len(u_stock_center)-1):
				StockParser(url,cookies,u_Arr_center,0).start()
				sum += len(u_Arr_center)
				u_Arr_center = []
		
	
		for stock in u_stock_cabinet:
			index = u_stock_cabinet.index(stock)
			u_Arr_cabinet.append(stock)
			if (len(u_Arr_cabinet) is len(u_stock_cabinet)/10) or (len(u_Arr_cabinet) > 99) or (index is len(u_stock_cabinet)-1):
				StockParser(url,cookies,u_Arr_cabinet,1).start()
				sum += len(u_Arr_cabinet)
				u_Arr_cabinet = []
	except KeyboardInterrupt:
		print "killing thread"

if __name__ == "__main__":
	main()