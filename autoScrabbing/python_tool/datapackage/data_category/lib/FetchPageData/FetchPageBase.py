# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FetchPageBase(object):
	"""Ftech Data Base class"""
	url  = None

	def __init__(self, driver):
		self.driver = driver
		if not self.driver:
			print "please initial the driver driver"

	def load_driver(self):
		self.driver.get(self.url)

	def set_url(self, url):
		self.url = url

	def close_connect(self):
		if self.url_driver:
			self.url_driver.close()

	'''Element Search function'''
	def wait_page_loading(self, XPATH):
		'''wait the page finish loading'''
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH)))


	def find_elements_by_id(self, id):
		'''id search'''
		return self.driver.find_elements(By.ID, id)

	def find_elements_by_name(self, name):
		'''name search'''
		return self.driver.find_elements(By.NAME, name)

	def find_elements_by_class(self, className):
		'''class name search'''
		return self.driver.find_elements(By.CLASS_NAME, className)

	def find_elements_by_css_selector(self, css_selector):

		return self.driver.find_elements(By.CSS_SELECTOR, css_selector)

	def find_elements_by_xpath(self, XPATH):
		'''XPATH search'''
		'''
			usage example:
			username = driver.find_element_by_xpath("//form[input/@name='username']")
			username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
			username = driver.find_element_by_xpath("//input[@name='username']")
			clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
			clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
		'''
		try:
			tempArr = []
			for element in self.driver.find_elements(By.XPATH, XPATH):
				tempArr.append(element.text)
			return tempArr
		except NoSuchElementException:
			return []

	def find_elements_by_link_text(self, link_text):
		'''will return the link(href)'''
		'''
			<a href="continue.html">Continue</a>
			the link_text should be "Continue"
		'''
		return self.driver.find_elements(By.LINK_TEXT, link_text)

	def is_exist(self, XPATH):
		try:
			self.driver.find_element(By.XPATH, XPATH)
			return True
		except NoSuchElementException:
			return False






		