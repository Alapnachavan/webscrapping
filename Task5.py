from Task1 import data
import json
import pprint
from bs4 import BeautifulSoup
import requests

movie_list_details=[]
# print(data)
for i in data:

    url=i['movie URL']

    def scrap_movie_detail(movie_url):
        # movie_url1=movie_url['Url']
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")
        # print(soup)
        title=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column")
        # print(title)
        title1=title.find('div',class_="thumbnail-scoreboard-wrap")
        # # print(title1)
        poster=title1.find('img',class_="posterImage js-lazyLoad")
        poster1=poster['src']
        # print(poster1)
        title2=title1.find('score-board',class_="scoreboard")
        # print(title2)
        name=title2.find("h1",class_="scoreboard__title" ).get_text()
        # print(name)
        s=soup.find('ul',class_="content-meta info")
        # print(s)
        genre=s.find('div',class_='meta-value genre').get_text().split()
        # print(genre)
        sub_tle=s.find_all('li',class_="meta-row clearfix")
        # print(sub_tle)
        movie_d={}
        movie_d['Name']=name

        for i in sub_tle:
            k=i.find('div',class_="meta-label subtle").get_text()
            key=k[:-1]
            # print(key)
            value=i.find('div',class_="meta-value").get_text().strip().replace(" ","").replace('\n',"").replace('\u00a0'," ")
            # print(value)
            movie_d['Name']=name
            movie_d[key]=value
        time=int(movie_d["Runtime"][0])*60
        for i in movie_d['Runtime'][2:]:
                if 'm' not in i:
                    time+=int(i)
                else:
                    break
        movie_d["Runtime"]=str(time)+' m'
        movie_d["Poster_image_url"]=poster1
        movie_list_details.append(movie_d)
        # movie_d["Original Language"]=movie_d["Original Language"].strip().split()
         # print(movie_list_details)
        movie_d["Genre"]=genre
        with open("Task5.json","w") as f:
            json.dump(movie_list_details, f,indent=6)
        # return movie_d
        return movie_list_details

    movie_list=scrap_movie_detail(url)


	
	
	
