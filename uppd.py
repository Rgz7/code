from selenium import webdriver
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

#//*[@id="J_ManageBody"]/nav/div/div[4]/ul/li[1]/a/span  20298100  curtain
#//*[@id="J_ManageBody"]/nav/div/div[4]/ul/li[2]/a/span


class upload:
	
	def __init__(self,):
		self.title = ""
		self.dsc = ""
		self.value1 = ""
		self.value2 = ""
		self.id = pymsgbox.prompt("输入商品已下载的商品id","提示")
		self.proName = pymsgbox.prompt("输入文件夹名称","提示")
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--ignore-certificate-errors')
		self.options.add_argument('--ignore-ssl-errors')
		self.driver = webdriver.Chrome(chrome_options=self.options)
		self.driver.get("http://mms.pinduoduo.com")
		sleep(3)
		self.popMsg()
		
	def loadData(self,):
		F = open("./{}/{}/data.txt".format(self.proName,self.id))
		for fline in F:
			if ("<title>:" in fline):
				self.title = fline.split("<title>:")[1]
			elif ("<dsc>:" in fline):
				self.dsc = fline.split("<dsc>:")[1]
			elif ("<value1>:" in fline):
				self.value1 = fline.split(":")[1]
			elif ("<value2>:" in fline):
				self.value2 = fline.split(":")[1]
			else:
				pass
		F.close()
		sleep(3)
	def popInput(self,msg,title):
		mssage = pymsgbox.prompt(msg,title)
		return mssage
		
		
	def popMsg(self,):
		ret = ctypes.windll.user32.MessageBoxW(0,"请手动登陆后台,然后再点击确定继续","提示",1)
		return ret
	
	def gotoproduct(self,):
		pNgoods = self.driver.find_element_by_xpath("//*[@id='J_ManageBody']/nav/div/div[4]/ul/li[1]/a/span")
		pNgoods.click()
		sleep(2)
		
		createNgoods = self.driver.searchCategory = self.driver.find_element_by_css_selector("a.pdd-btn.g-e-t-b-creat-btn")
		createNgoods.click()
		sleep(3)
		
		for handle in driver.window_handles:
			self.driver.switch_to_window(handle)
		sleep(3)
	def slectCategory(self,):
		category = self.driver.find_element_by_xpath("//*[@id='searchInput']")
		category.send_keys("床帘")
		searchCategory = self.driver.find_element_by_css_selector("div.pdd-btn.search-btn")
		searchCategory.click()

		sleep(2)
		slect = self.driver.find_element(By.XPATH,'//td[text()="床幔"]')
		slect.click()
		sleep(1)
		muiButton = self.driver.find_element_by_class_name("bottom")
		muiButton.click()


	#write title
	#must given a product id 
	def Title(self,):
		t = self.driver.find_element_by_class_name("mui-form-group-input")
		t.send_keys(str(self.title))

		sleep(2)

		#----------check image sieze------------
	def mainImage(self,):
		Mimage = []
		filelist = os.listdir("./{}/{}/Gallery/".format(self.proName,self.id))
		for i in filelist:
			img = Image.open("./curtain/{}/Gallery/{}".format(self.id,i))
			if (img.size[0] == img.size[1]):
				Mimage.append(i)
	#upload main image
		
		loopPic = self.driver.find_element_by_xpath("//input[@type='file']")		
		for mImage in Mimage:
			loopPic.send_keys("{}\\{}\\{}\\Gallery\\{}".format(os.cwd(),sef.proName,self.id,mImage))
			sleep(2)
	
	#-----------write textual describe ---------

	def txtdsc(self,):
		Tdescribe = self.driver.find_element(By.XPATH,'//p[text()="填写更多图文详情"]')
		Tdescribe.click()
		sleep(1)
		wTextDescribe = self.driver.find_element_by_class_name("mui-form-group-textarea")
		wTextDescribe.send_keys(self.dsc)
		sleep(1)
	#------upload detail describe image --------
	def detailImage(self,):
		
		detailimage = []
		countnum = []
		filelist = os.listdir("./curtain/{}/Gallery/".format(self.id))
		for dtimg in filelist:
			img = Image.open("./curtain/{}/Gallery/{}".format(self.id,dtimg))
			if (img.size[0] != img.size[1]):
				detailimage.append(dtimg)
		for toINT in detailimage:
			countnum.append(int(toINT.split(".")[0]))
		countnum.sort()
		countnum.reverse()
		detailIMG = self.driver.find_element_by_xpath("//*[@id='goods-basic']/div[3]/div/div[4]/div[3]/div/div/div/input")
		for dtimage in countnum:
			detailIMG.send_keys("{}\\{}\\{}\\Gallery\\{}".format(os.cwd(),self.proName,self.id,str(dtimage)+".jpeg"))
			sleep(2)
	
	#-----add sku -------
	def addSku(self,):
	
		addSkuBtton = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[3]/button")
		addSkuBtton.click()
		sleep(1)
		clickSelect = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/span")
		clickSelect.click()
		list = self.driver.find_element_by_xpath("//li[text()='{}']".format("颜色"))
		list.click()
		sleep(2)
		#add  first option -----
		writepty = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/input")
		morepty = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[1]/div[2]/div/a")
		v1 = re.findall("\'(.+?)\'",self.value1)
		for v in v1:
			writepty.send_keys(v)
			writepty.send_keys(Keys.RETURN)
			sleep(1)

	##______option 2_____
		sleep(1)
		secondpty = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[3]/button")
		secondpty.click()
		sleep(1)

		clickSecond = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/span")
		clickSecond.click()
		sleep(2)
		list2 = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/input")
		list2.send_keys("套餐")
		list2.send_keys(Keys.RETURN)
		sleep(2)
		writeSecondpty = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/input")
		morepty2 = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[2]/div/div/div[2]/div[2]/div/a")



		v2 = re.findall("\'(.+?)\'",self.value2)
		for v2 in value1:
			writeSecondpty.send_keys(v2)
			writeSecondpty.send_keys(Keys.RETURN)
			sleep(1)
		sleep(1)
		setStorge = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/div/div/input")
		sleep(1)
		setStorge.send_keys("500")
		
		storgeButton = self.driver.find_element_by_xpath("//*[@id='sku']/div[2]/div[3]/div[1]/div/div/a")
		storgeButton.click()
		sleep(2)



	def saveproduct(self,):
		

		#save writer
		saveProduct = driver.find_element_by_xpath("//*[@id='goods_create']/div[1]/div/div[2]/div[6]/button[2]")
		saveProduct.click()
		sleep(2)

		driver.close()
	
UL = upload()

UL.loadData()
while (True):
	try:
		UL.gotoproduct()
	except:
		print("error")
		break
	try:
		UL.slectCategory()
	except:
		print("error")
		break
	try:
		UL.Title()
	except:
		print("error")
		break
	try:
		UL.mainImage()
	except:
		print("error")
		break
	try:
		UL.txtdsc()
	except:
		print("error")
		break
	try:
		UL.detailImage()
	except:
		print("error")
		break
	try:
		UL.addSku()
	except:
		print("error")
		break
	try:
		UL.saveproduct()
	except:
		print("error")
		break
	print("nice")
	break
	
	
	
	
	
	
	
	




