from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep 
from PIL import Image
import os
import re
import ctypes
import pymsgbox

class KD:
	def __init__(self,url):
		self.driver = webdriver.Chrome()
		self.driver.get(url)
		sleep(1)
		
		self.search = self.driver.find_element_by_xpath("//*[@id='mailNo']")
		self.schBu = self.driver.find_element_by_xpath("//*[@id='submitButton']")
		
		self.line_Begin = "#{}----"
		self.line_End = "end----"
	def sv(sefl,data):
		file = open("post.txt","a")
		file.write(data+"\n")
		file.close()
	
	def YD(self,num):
		self.sv(self.line_Begin.format(num))
		search.send_key(postNum)
		sleep(1)
		schBu.click()
		sleep(1)
		table = self.driver.find_element_by_xpath("//*[@id='result']/table/tbody")
		self.sv(table.text)
		self.sv(self.line_End)

		
