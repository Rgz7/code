#!D:\python\python.exe

import os 
import cgi
import codecs,sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) # option for non-english page

form = cgi.FieldStorage()

parementValue = form.getvalue("parementName")  #get parement from url


print("Content-Type:text/html")
print()
print("<TITLE>Cgi script output</TITLE>")
print("<H1>Display the server respone</H1>")
print("<h2>{}</h2>".format(program))

#add your script here
