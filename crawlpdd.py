import re
import os
import json
import requests
from time import sleep,ctime
import urllib
import sqlite3
#urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
class Pdd:
	def __init__(self,keyWords,subwayID):
		self.keyWords = keyWords
		self.subwayID = subwayID
		self.subway = None
		self.shopSale = './shop/'
		
		self.header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
	
	def connectToWeb(self,url):
		session = requests.Session()
		req = session.get(url,headers=self.header)
		return req.text
	
		
	def getProduct(self):
		counts = 0
		items = 'items'
		goodsName = 'goods_name'
		country = 'country'
		goods_id = 'goods_id'
		sales = 'sales'
		normal_price = 'normal_price'
		Price = 'price'
		url = "http://apiv3.yangkeduo.com/search?q="+self.keyWords+"&requery=0&page=1&size=20&sort=default&pdduid=2551530916"
		rejson = json.loads(str(self.connectToWeb(url)))
		while (counts < len(rejson.get('items'))):
			#GN = rejson.get(items)[counts].get(goodsName)
			GID = rejson.get(items)[counts].get(goods_id)
			SAL = rejson.get(items)[counts].get(sales)
			NP = rejson.get(items)[counts].get(normal_price)
			price = rejson.get(items)[counts].get(Price)
			counts = counts + 1
			
			for i in self.subwayID:
				if (str(GID) == i.replace('\n','')):
					f = open('./shop/'+projectName+'/subway/'+self.keyWords.replace('\n','')+'.txt','a')
					f.write(self.keyWords.replace('\n','') + '\t' + i.replace('\n','') + '\t' + str(counts) + '\n')
					f.close()
					print(i,'subway>>>>>',counts)
			self.saveData(GID,SAL,NP,price)
		cutline = open('subway.txt','a')
		cutline.write('----------------------------' + '\n')
		cutline.close()
			
		print('Done!...subway:',self.subway)
	
	def checkdata(self,gooID):
		
	
	def saveData(self,Gid,Sale,Nprice,price):
		

class databases:
	'''
	connect to databases,
	create table,
	insert data to table,
	'''
	def __init__(self):
		pass
	def idinfotable(self,proinfo,id)
		#create product id info table
		command = '''create table {} (id PRIMARY KEY,title VARCHAR(255),goodsid INT,sale INT,np INT,price INT)'''.format(id)
		conn = sqlite3.connect(proinfo+".db")
		cursor = conn.curosr()
		cursor.execute(command)
		conn.commit()
		conn.close()
	def idinfoinser(self,data):
		
	
	
def checkprogram(dir):
	dirfound = False
	for i in os.listdir('./shop/'):
		if (i == dir):
			dirfound = True
			break
	return dirfound 

def start(gkey,gID):
	while True:
		timeset = 10 * 60
		for gk in gkey:
			spider = Pdd(gk.replace('\n',''),gID)
			spider.getProduct()
		sleep(timeset)
	
