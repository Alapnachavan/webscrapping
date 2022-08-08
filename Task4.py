from bs4 import BeautifulSoup
import requests
import json
def scrap(url):
    d1={}
    u=[]
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')

    for ul in soup.find_all('a', class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"):
      u.append(ul.get_text())
    list=["Hindi","English","Tamil","Telugu","Malayalam","Kannada","Bengali"]
    hh=[]
    for i in u:
        for j in list:
            if i==j:
                hh.append(i)
    

    movie_name=soup.find("div",class_="sc-94726ce4-2 khmuXj").h1.get_text()
    d1["movie_name"]=movie_name

    d1["language"]=hh

    runtime=soup.find("div",class_="sc-94726ce4-3 eSKKHi").get_text().strip()
    u=runtime[-6:]
    # a=u[3:5]
    # f=int(u[0])*60
    # s=(f+int(a),"minute")
    d1["Runtime"]=u

    bio=soup.find("div",class_="sc-16ede01-7 hrgVKw").get_text()
    d1["bio"]=[bio]

    director=soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
    d1["Director"]=[director]
    # print(director)

    poster_image=soup.find("div",class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img").img['src']
    d1["postername"]=poster_image

    abc=soup.find('div',class_="ipc-chip-list__scroller")
    ga=abc.find_all('span')
    list1=[]
    for i in ga:
        list1.append(i.get_text())
    d1['genre']=list1

    Detail=soup.find("section",cel_widget_id="StaticFeature_Details")
    s=Detail.find_all("div")
    y=[]
    for ul in s:
        h=ul.find_all("ul")
        for li in h:
            o=li.find_all("li")
            for aa in o:
                z=aa.find_all('a')
                dtails=[details.get_text() for details in z]
                for p in dtails:
                 y.append(p)
    d1["country"]=y[5]
    b=y[1].split()
    d1["release_year"]=b[2]
    d1["release_date"]=b[1]+b[0]
    return d1
url= "https://www.imdb.com/title/tt9263550/"
bb=scrap(url)
with open("task4.json","w")as h:
    g=json.dump(bb,h,indent=2)