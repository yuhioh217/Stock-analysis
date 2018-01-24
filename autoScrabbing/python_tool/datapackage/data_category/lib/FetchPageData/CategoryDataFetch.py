from FetchPageBase import FetchPageBase
import re

class CategoryDataFetch(FetchPageBase):
 	"""docstring for CategoryDataFetch"""
 	url = "http://jdata.yuanta.com.tw/z/zh/zhc/zhc.djhtm?"
 	def set_page(self, itemId):
 		all_url = '{}a={}'.format(self.url, itemId)
 		print "----" + itemId + "----"
 		self.set_url(all_url)
 		self.load_driver()

 	def get_stock_info(self):
 		self.wait_page_loading("//table[@id='oMainTable']")
 		return self.find_elements_by_xpath("//td[@id='oAddCheckbox']")


