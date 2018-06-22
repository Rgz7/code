import re
import os
import json
import requests
from time import sleep,ctime
import urllib
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
		
		file = open('.\/shop\/'+projectName+'/'+str(gooID)+'.txt','r',encoding='utf-8')
		
		for i in file:
			lastSale = i.split('\t')[0]
		file.close()
		return lastSale
		
	
	def saveData(self,Gid,Sale,Nprice,price):
		if ((str(Gid)+'.txt') in os.listdir('.\/shop\/'+projectName+'/')):
			a = self.checkdata(Gid)
			if (str(Sale) == str(a.split('>')[0])):
				print('Sale no change')
				
			else:
				
				cmp = int(str(Sale)) - int(str(a.split('>')[0]))
				file = open('.\/shop\/'+projectName+'/'+str(Gid)+'.txt','a+',encoding='utf8')
				string = str(Sale) + '>' + str(cmp) + '\t' + str(Nprice) + '|' + str(price) + '\n'
				file.write(string)
				print('Save change',Gid)
				file.close()
		else:
			file = open('.\/shop\/'+projectName+'/'+str(Gid)+'.txt','a+')
			string = str(Sale) + '\t' + str(Nprice) + '|' + str(price) + '\n'
			file.write(string)
			print('New log save',Gid)
			file.close()

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
	
def createProgram(pgrName):
	path = './shop/'+pgrName
	subwaypath = './shop/'+pgrName+'/subway/'
	
	os.mkdir(path)
	os.mkdir(subwaypath)
	id = []
	key = []
	ids = input('Add id:')
	while(ids != ''):
		id.append(ids)
		ids = input('Add id:')
	
	keys = input('Add key:')
	while(keys != ''):
		key.append(keys)
		keys = input('Add key:')
	filekey = open(path+'/key.txt','a+')
	for i in key:
		filekey.write(i+'\n')
	filekey.close()
	fileid = open(path+'/id.txt','a+')
	for a in id:
		fileid.write(a+'\n')
	fileid.close()

global projectName	
	
getkey = []
getID = []

projectName = input("Program:")
if(checkprogram(projectName)):
	fileid = open('.\/shop\/'+projectName+'/'+'id'+'.txt','r')
	for shopid in fileid:
		getID.append(shopid)
	fileid.close()
	filekey = open('.\/shop\/'+projectName+'/'+'key'+'.txt','r')
	for shopkey  in filekey:
		getkey.append(shopkey)
	filekey.close()
	start(getkey,getID)
	
else:
	print("Create new program")
	answer = input("Are you sure to create a program?  y|n")
	if (str(answer) == 'y'): 
		createProgram(projectName)
		
		fileid = open('.\/shop\/'+projectName+'/'+'id'+'.txt','r')
		for shopid in fileid:
			getID.append(shopid)
		fileid.close()
		filekey = open('.\/shop\/'+projectName+'/'+'key'+'.txt','r')
		for shopkey  in filekey:
			getkey.append(shopkey)
		filekey.close()
		start(getkey,getID)
	else:
		print("Bye")

