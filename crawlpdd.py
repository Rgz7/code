import re
import os
import json
import requests
from time import sleep,ctime
import urllib
import sqlite3
#urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
class Pdd:
	def __init__(self,keyWords,filename):
		self.keyWords = keyWords
		self.filename = filename
		self.header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
	
	def createTable(self,id):
		#create product id info table
		command = '''create table {} (id INT PRIMARY KEY,goodsid INT,sale INT,np INT,price INT)'''.format(id)
		conn = sqlite3.connect(self.filename+".db")
		cursor = conn.cursor()
		cursor.execute(command)
		conn.commit()
		conn.close()
	def inserData(self,id,dic):
		
		conn = sqlite3.connect(self.filename+".db")
		cursor = conn.cursor()
		cursor.execute("select max(id) from {}".format(id))
		c = cursor.fetchall()
		if (c[0][0] == None):
			command = '''insert into {} values ({},{},{},{},{})'''.format(id,1,int(dic["goodsid"]),int(dic["sale"]),int(dic["np"]),int(dic["price"]))
			cursor.execute(command)
			conn.commit()
		else:
			command = '''insert into {} values ({},{},{},{},{})'''.format(id,c[0][0]+1,int(dic["goodsid"]),int(dic["sale"]),int(dic["np"]),int(dic["price"]))
			cursor.execute(command)
			conn.commit()
		conn.close()
		return 1
	def checkID(self,id):
		found = False
		command = '''select name from sqlite_master where type="table"'''
		conn = sqlite3.connect(self.filename+".db")
		cursor = conn.cursor()
		cursor.execute(command)
		c = cursor.fetchall()
		lenth = len(c)
		count = 0
		while(count < lenth):
			if ((id) == ("_"+str(c[count][0]))):
				found = True
			count += 1
		conn.close()
		return found
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
			if (self.checkID("_"+str(GID)) == False):
				#(id PRIMARY KEY,title VARCHAR(255),goodsid INT,sale INT,np INT,price INT)
				self.createTable("_"+str(GID))
				#dic["id"],dic["title"],dic["goodsid",dic["sale"],dic["np"],dic["price"]
				dic = {"goodsid":str(GID),"sale":str(SAL),"np":str(NP),"price":str(price)}
				self.inserData("_"+str(GID),dic)
			

			
class subway:
	def __init__(self,filename)
keyw = input("keyword:")
fn = input("filename")		
	
	
start = Pdd(keyw,fn)
start.getProduct()

