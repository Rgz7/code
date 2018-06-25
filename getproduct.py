import re
import os
import json
import sys
import requests
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse,unquote,unquote_plus
try:
	import wget
except:
	os.system("pip install wget")
	import wget


class PddSpider:
	""" A spider to crawl data from pdd """
	
	def __init__(self,id):
		self.keywords = id
		#shop init
		
		self.mall_name = 'mall_name'
		self.mall_sales = 'mall_sales'
		self.header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
		self.pageresult = self.connectToWeb("http://apiv4.yangkeduo.com/v5/goods/"+self.keywords)
	def saveData(self,textcontent):
		file = open("./{}/{}/data.txt".format(rootFile,projectName),'a')
		file.write(str(textcontent)+"\n")
		file.close()
	def connectToWeb(self,url):
		session = requests.Session()
		req = session.get(url,headers=self.header)
		return req.text
	def getProductDetail(self):

		goodsID = "goods_id"
		goodsNname = "goods_name"
		goodsDesc = "goods_desc"
		hdImage = "hd_thumb_url"
		image_url = "image_url"
		GI = json.loads(self.pageresult).get(goodsID)
		GN = json.loads(self.pageresult).get(goodsNname)
		GD = json.loads(self.pageresult).get(goodsDesc)
		HI = json.loads(self.pageresult).get(hdImage)
		IU = json.loads(self.pageresult).get(image_url)
		HIfilename = HI.split('/')[-1]
		IUfilename = IU.split('/')[-1]
		
		os.system("python -m wget -o ./{}/{}/{}/{} {}".format(rootFile,projectName,mainFile,HIfilename,HI))
		os.system("python -m wget -o ./{}/{}/{}/{} {}".format(rootFile,projectName,mainFile,IUfilename,IU))
		self.saveData(str(GI))
		self.saveData(GN)
		self.saveData(GD)
		print(GI,GN,GD)
		
			
	def productSku(self):
	
		initcount = 0
		thumb_url = "thumb_url"
		normal_price = "normal_price"
		group_price = "group_price"
		spec_key = "spec_key"
		spec_value = "spec_value"
		layercount = 0
		listmember = 0
		keylist = []
		value2 = []
		value1 = []
		price = []
		# get lenth of list
		while (initcount < len(json.loads(self.pageresult).get('sku'))):
			TU = json.loads(self.pageresult).get('sku')[initcount].get(thumb_url)
			NP = json.loads(self.pageresult).get('sku')[initcount].get(normal_price)
			GP = json.loads(self.pageresult).get('sku')[initcount].get(group_price)
			#self.saveData("normalPrice------->>"+str(NP/100))
			#self.saveData("groupPrice-------->>"+str(GP/100))
			filetype = TU.split('/')[-1].split('.')[-1]
			os.system("python -m wget -o ./{}/{}/{}/{}.{} {}".format(rootFile,projectName,skuFile,initcount,filetype,TU))
			
				#get lenth of specs key list 
			for i in range(0,len(json.loads(self.pageresult).get('sku')[initcount].get("specs"))):
				SK = json.loads(self.pageresult).get('sku')[initcount].get("specs")[i].get(spec_key)
				SV = json.loads(self.pageresult).get('sku')[initcount].get("specs")[i].get(spec_value)
				if(SK not in keylist):
					if(layercount < 3):
						layercount = layercount + 1
				if(SK not in keylist):
					keylist.append(SK)
					listmember += 1
				if((layercount == 1) | (listmember == 1)):
					if(SV not in value1):
						value1.append(SV)
					layercount += 1
				elif((layercount == 2) | (layercount == 3)):
					if(layercount == 3):
						if(SV not in value2):
							value2.append(SV)
						layercount -= 2
					elif(layercount == 2):
						if(SV not in value2):
							value2.append(SV)
						layercount -=1
				
				
				self.saveData("specKey---->>>"+SK)
				self.saveData("specValue----->>>"+SV)			
				print(SK,SV)
			self.saveData("normalPrice------->>"+str(NP/100))
			self.saveData("groupPrice-------->>"+str(GP/100))
			pr = str(NP/100)+":"+str(GP/100)
			if (pr not in price):
				price.append(pr)
			print(TU,NP,GP)
			initcount = initcount + 1
		self.saveData(keylist)
		self.saveData(value1)
		self.saveData(value2)
		self.saveData(price)
	def productGallery(self):
		#get lenth of list
		ZERO = 0
		imagecount = 0
		listofgallery = []
		galleryurl = "url"
		
		while (ZERO < len(json.loads(self.pageresult).get('gallery'))):
			GU = json.loads(self.pageresult).get('gallery')[ZERO].get(galleryurl)
			listofgallery.append(GU)
			ZERO = ZERO + 1
		for galleryLink in listofgallery:
			filetype = galleryLink.split('/')[-1].split('.')[-1]
			os.system("python -m wget -o ./{}/{}/{}/{}.{} {}".format(rootFile,projectName,galleryFile,imagecount,filetype,galleryLink))
			print(galleryLink,"save!")
			imagecount = imagecount + 1
		return True
	def productSale(self):
		sales = "sales"
		SL = json.loads(self.pageresult).get(sales)
		self.saveData("Sales:"+str(SL))
		print(SL)
		return True
def createFile(PJN):
	os.system("mkdir .\\{}\\{}".format(rootFile,PJN))
	os.system("mkdir .\\{}\\{}\\{}".format(rootFile,PJN,galleryFile))
	os.system("mkdir .\\{}\\{}\\{}".format(rootFile,PJN,skuFile))
	os.system("mkdir .\\{}\\{}\\{}".format(rootFile,PJN,mainFile))
def createRootFile(projectName):
	#os.system("mkdir .\\{}\\{}".format(rootFile,PJN))
	os.system("mkdir .\\{}".format(rootFile))
global galleryFile,skuFile,mainFile,projectName,rootFile
galleryFile = "Gallery"
skuFile = "Sku"
mainFile = "Main"
rootFile = sys.argv[3]
projectName = sys.argv[1]
projectID = sys.argv[2]
if(rootFile not in os.listdir("./")):
	createRootFile(rootFile)
if(projectID not in os.listdir("./{}".format(rootFile))):
	createFile(projectName)
	crawl = PddSpider(projectID)
	crawl.productSale()
	crawl.getProductDetail()
	crawl.productGallery()
	crawl.productSku()
else:
	print("Project exit!")
