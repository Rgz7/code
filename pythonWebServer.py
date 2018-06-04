import os

#run http server
if ("cgi-bin" not in os.listdir()):
  os.mkdir("cgi-bin")
#save your cgi script in the cgi-bin directory
os.system("python -m http.server --bind localhost --cgi 8081")
