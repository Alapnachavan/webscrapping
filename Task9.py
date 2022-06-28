from Task1 import data
import os 
import json
import requests
import random
import time
import pprint
from bs4 import BeautifulSoup
url_list=[]
for i in data:
    url_list.append(i["movie URL"])
def get_movie_list_details(ulist):
    last=[]
    time_sleep=random.randint(1,3)
    for i in ulist:
        id=i[33:]
        if os.path.exists(id+".json")== True:
            with open(id+".json","r") as movieDataFile:
                data=movieDataFile.read()
                final=json.loads(data)
            last.append(final)
        else:
            final={}
            time.sleep(time_sleep)
            LinkData=requests.get(i)
            soup=BeautifulSoup(LinkData.text,"html.parser")
            final["name"]=soup.find("h1").text
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            for i in all:
                final[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.replace(" ","").replace("\n","").strip()
            with open(id+"Task_9.json","w") as file:
                json.dump(final,file,indent=2)
            last.append(final)
    return last
get_movie_list_details(url_list)