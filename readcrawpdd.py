import os 
import sqlite3




class rd:
	def __init__(self):
		self.datapath = "./db"
		self.database = ''
		
		
	def execute(self,command):
		conn = sqlite3.connect(self.database)
		cursor = conn.cursor()
		cursor.execute(command)
		result = cursor.fetchall()
		conn.close()
		
		return result
	def displaysub(self,keys):
		cmd = '''select name from sqlite_master where type="table"'''

		resp = self.execute(cmd)
		for tbname in resp:
			if ("_" in tbname[0]):
				getkeyword = '''select * from {} where kw = {}'''.format(tbname[0],keys)
				resp = slef.execute(getkeyword)
	def read(self):
		db = os.listdir(self.datapath)
		for dbname in db:
			if ("sub.db" in dbname):
				cmd = "select key from keyword"
				self.database = dbname
				resp = self.execute(cmd)
				for ky in resp:
					slef.displaysub(ky[0])
				
