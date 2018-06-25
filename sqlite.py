def createTable():
	command = """CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL, 
				NAME TEXT NOT NULL,
				AGE INT NOT NULL)"""
	cursor = conn.cursor()
	cursor.execute(command)
	conn.commit()

def inserdata(id):
	command = """INSERT INTO COMPANY (ID,NAME,AGE) 
					VALUES ({},'销量',66)""".format(id)
	cursor = conn.cursor()
	cursor.execute(command)
	conn.commit()

def updateData():
	command = "UPDATE COMPANY SET NAME = 'gg' where ID = 6"
	cursor = conn.cursor()
	cursor.execute(command)
	conn.commit()
	
def showdata(id=None,name=None,age=None):
	cursor = conn.cursor()
	logcount = 0
	select = "SELECT * FROM COMPANY WHERE ID = max(ID)"
	result = cursor.execute(select)
	check = type(result)
	print(check)
	for i in result:
		print(i)
		logcount += 1
	
	print(logcount)
def delete(id):
	cursor = conn.cursor()
	command = "delete from COMPANY where ID = {}".format(id)
	cursor.execute(command)
	conn.commit()
