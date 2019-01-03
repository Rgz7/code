import pyautogui as mygui
import os
import webview

import threading
from pynput.keyboard import Key,Listener
from time import sleep


page = '''
		<!DOCTYPE html>
		<html>
		<head lang="en">
		<meta charset="UTF-8">
		<style>
			body {
				background-color: black;
				color: green;
			
			}
		</style>
		</head>
		<body onload="getDirImg()">
		<script>
		function showResponse(response) {
			var container = document.getElementById('resultPage')

			container.innerText = response.message
			container.style.display = 'block'
		}
		function getDirImg() {
			pywebview.api.getDirImg().then(showResponse)
		}
		function GetBrowserPosition() {
			pywebview.api.keyMon("GetBrowserPosition").then(showResponse)
			
		}
		function GetPhoneNumberPosition() {
			pywebview.api.keyMon("GetPhoneNumberPosition").then(showResponse)
			
		}
		function send() {
			pywebview.api.keyMon("GetSendPosition").then(showResponse)
		}
		function run() {
			pywebview.api.run().then(showResponse)
		}
		</script>
		
		<div id="img">Img resource</div>
		<div id="browserTag">浏览器位置坐标</div>
		<button onclick="GetBrowserPosition()">获取浏览器位置</button>
		
		<div id="phoneNumberPosition">手机号坐标</div>
		<button onclick="GetPhoneNumberPosition()">获取手机号坐标</button>
		
		<div id="sendSMS">发送短信坐标</div>
		<button onclick="send()">发送短信坐标</button>
		<button onclick="run()">启动</button>
		<div>
		<p>按键记录></p>
		<p id="keypress"></p>
		</div>
		
		</body>
		</html>
		'''

class webJSapi:
	def __init__(self):
		self.position = {}
		self.actionCheck = ""
		self.record = []
		self.listimg = os.listdir("./img/")
		
		self.imgdir = "./img/"
		self.secreenWidth,self.screenHeight = mygui.size()
		self.currentMouseX,self.currentMouseY = mygui.position()
		
	def getDirImg(self,nothing):
		webview.evaluate_js('''document.getElementById("img").innerHTML = "{}" '''.format(self.listimg))
		
	def keyMon(self,positionCheck):
		with Listener(on_press=self.on_press) as listener:
			self.actionCheck = positionCheck
			listener.join()
		return {"message":"key mon end!"}
	def on_press(self,key):
		webview.evaluate_js('''document.getElementById("keypress").innerHTML = "{}" '''.format(key))
		
		if (key == Key.esc):
			if (self.actionCheck == "GetBrowserPosition"):
				self.position["GetBrowserPosition"] = self.record
				webview.evaluate_js('''document.getElementById("browserTag").innerHTML = "{}" '''.format(self.record))
				self.record = []
			elif (self.actionCheck == "GetPhoneNumberPosition"):
				self.position["GetPhoneNumberPosition"] = self.record
				webview.evaluate_js('''document.getElementById("phoneNumberPosition").innerHTML = "{}" '''.format(self.record))
				self.record = []
			elif (self.actionCheck == "GetSendPosition"):
				self.position["GetSendPosition"] = self.record
				webview.evaluate_js('''document.getElementById("sendSMS").innerHTML = "{}" '''.format(self.record))
				self.record = []
			else :
				pass 
			print(self.position)
			return False
			
		self.record.append(mygui.position())
		print(mygui.position())
class autoGUI:
	def __init__(self,html):
		self.html = html
		self.create_app()
		
		
	def create_app(self):
		t = threading.Thread(target=self.htmlpage)
		t.start()
		
		js = webJSapi()
		webview.create_window('API example', js_api=js)
		print("windows off")
	def htmlpage(self):
		webview.load_html(self.html)
	
app = autoGUI(page)
