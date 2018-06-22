import re
import os
import json
import requests
from time import sleep,ctime
import urllib
import sqlite3

class DB:
	def __init__(self,dbName,tbName):
		self.dbname = dbName
		self.tbname = tbNmme
		
	def condb(self,command,args=""):
		conn = sqlite3.connect(self.dbname)
		print("ok")
		cursor = conn.cursor()
		if (command == "maxId"):
			cursor.execute("select max(ID) from ?",self.tbname)
			result = c.fetchone()
		elif (command == "proIndex"):
			cursor.execute("select * from ? where index = ?",self.tbname,args)
			result = c.fetchone()
		else:
			result = 0
		conn.close()
		return result
		

class createProgram:
	def __init__(self,name):
		self.name = name
		self.projectdb = "projectIndex.db"
		self.projecttb = "index"
	def checkprogram():
		checkname = False
		linkdb = DB(self.projectdb,self.projecttb)
		linkdb.condb("proIndex",self.name)
			checkname = True
		return checkname 
	


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
