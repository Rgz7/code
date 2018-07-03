import re
import os
import json
import requests
from time import sleep,ctime
import urllib
import sqlite3
import time 
#urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
class Pdd:
	def __init__(self,keyWords,filename):
		self.keyWords = keyWords
		self.filename = "./db/"+filename
		self.header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
	
	def createTable(self,id):
		#create product id info table
		command = '''create table {} (id INTEGER PRIMARY KEY,goodsid INT,sale INT,np INT,price INT)'''.format(id)
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
			command = '''insert into {} values (NULL,{},{},{},{})'''.format(id,int(dic["goodsid"]),int(dic["sale"]),int(dic["np"]),int(dic["price"]))
			cursor.execute(command)
			conn.commit()
		else:
			command = '''insert into {} values (NULL,{},{},{},{})'''.format(id,int(dic["goodsid"]),int(dic["sale"]),int(dic["np"]),int(dic["price"]))
			cursor.execute(command)
			conn.commit()
		conn.close()
		return 1
		
	def getbigvalue(self,id,sal):
		conn = sqlite3.connect(self.filename+".db")
		cursor = conn.cursor()
		cursor.execute("select max(id) from {}".format(id))
		c = cursor.fetchall()
		cursor.execute("select sale from {} where id = {}".format(id,c[0][0]))
		c = cursor.fetchall()
		conn.close()
		c = int(c[0][0])
		if (int(sal) == c):
			return False
		else:
			return c
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
			if ((id) == (str(c[count][0]))):
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
			dic = {"goodsid":str(GID),"sale":str(SAL),"np":str(NP),"price":str(price)}
			loccheck = subway(self.filename+"sub",self.keyWords)
			loccheck.checkloc("_"+str(GID),counts)
			if (self.checkID("_"+str(GID)) == False):
				#(id PRIMARY KEY,title VARCHAR(255),goodsid INT,sale INT,np INT,price INT)
				self.createTable("_"+str(GID))
				#dic["id"],dic["title"],dic["goodsid",dic["sale"],dic["np"],dic["price"]
				self.inserData("_"+str(GID),dic)
				print("NEW LOG!")
			else:
				lastvalue = self.getbigvalue("_"+str(GID),SAL)
				if (lastvalue == False):
					pass
				else:
					self.inserData("_"+str(GID),dic)
					print(GID,"Sales increase>>",SAL - lastvalue)

			
class subway:
	def __init__(self,filename,kw = None):
		self.finename = filename
		self.kw = kw
	def keylist(self):
		conn = sqlite3.connect(self.finename+".db")
		cursor = conn.cursor()
		cursor.execute("create table keyword (id INTEGER PRIMARY KEY,key TEXT)")
		conn.commit()
		ins = input("addkeyword:")
		while (ins != ""):
			cursor.execute('''INSERT INTO keyword VALUES (NULL,'{}')'''.format(ins))
			conn.commit()
			ins = input("addkeyword:")
		conn.close()
	def idlist(self):
		conn = sqlite3.connect(self.finename+".db")
		cursor = conn.cursor()
		createid = input("subway-id:")
		while (createid != ""):
			cursor.execute("create table _{} (id INTEGER PRIMARY KEY,loc INT,kw VARCHAR(255))".format(createid))
			conn.commit()
			createid = input("subway-id:")
		conn.close()
	
	def checkloc(self,id,location):
		conn = sqlite3.connect(self.finename+".db")
		cursor = conn.cursor()
		cursor.execute('''select name from sqlite_master where type="table"''')
		rs = cursor.fetchall()
		
		for i in rs:

			if (i[0] == id):
				cursor.execute('''INSERT INTO {} VALUES (NULL,'{}','{}')'''.format(id,location,self.kw))
				conn.commit()
		conn.close()
	def selectData(self,args):
		if (args == "keys"):
			command = "select key from keyword"
		elif (args == "idlist"):
			command = "select id from idlist"
		conn = sqlite3.connect(self.finename+".db")
		cursor = conn.cursor()
		cursor.execute(command)
		c = cursor.fetchall()
		conn.close()
		return c 
		
	


	
def main(filename):
	if("db" not in os.listdir("./")):
		os.mkdir("db")
		
	if ((filename+".db") in os.listdir("./db/")):
		count = 0
		sb = subway("./db/"+filename+"sub")
		keylist = sb.selectData("keys")
		l = len(keylist)
		while (count < l):
			start = Pdd(keylist[count][0],filename)
			start.getProduct()
			count += 1
	else:
		nb = subway("./db/"+filename+"sub")
		nb.keylist()
		nb.idlist()
		count = 0
		sb = subway("./db/"+filename+"sub")
		keylist = sb.selectData("keys")
		l = len(keylist)
		while (count < l):
			start = Pdd(keylist[count][0],filename)
			start.getProduct()
			count += 1
fn = input("filename")
while(True):		
	main(fn)
	time.sleep(60 * 5)
	


	



