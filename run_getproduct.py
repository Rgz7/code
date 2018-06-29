import re
import os
import urllib.request
import json
import requests
#urllib.request.urlretrieve(image_url,full_file_name)




keyword = []
inputkeyword = input("type a keyword")

while (inputkeyword != ''):
        keyword.append(inputkeyword)
        inputkeyword = input("type a keyword")

os.system("mkdir {}".format(inputkeyword))
header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
for k in keyword:
        url = "http://apiv3.yangkeduo.com/search?q="+k+"&requery=0&page=1&size=20&sort=default&pdduid=2551530916"
        session = requests.Session()
        req = session.get(url,headers=header)
        i = 0
        while (i < len(json.loads(req.text).get('items'))):
                try:
                        t = json.loads(req.text).get('items')[i].get('ad').get('keyword')
                        print(t)
                        #saveto(t)
                except:
                        pass
                ID = json.loads(req.text).get('items')[i].get('goods_id')
                os.system("python getproduct.py {} {} {}".format(ID,ID,k))
                i = i + 1

print("Thankyou bye!")
