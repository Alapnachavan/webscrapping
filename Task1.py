from bs4 import BeautifulSoup
import requests
import json
import pprint
def adventure_movie():
    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    adventure_api=requests.get(adventure_url)

    htmlcontent=adventure_api.content
    soup=BeautifulSoup(htmlcontent,"html.parser")
    table_tag=soup.find("table",class_="table")
    tr=table_tag.find_all("tr")
    top_movie=[]
    for i in tr: 
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in  movie_rating:
            rating=rate.get_text().strip()
        movie_name=i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            movie_name=title
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text().strip()
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            url=requests.get(movie_link)
            htmlcontent=url.content
            soup=BeautifulSoup(htmlcontent,"html.parser")
            wrap=soup.find("div",class_="col mob col-center-right col-full-xs mop-main-column")
            cd=wrap.find("div",class_="thumbnail-scoreboard-wrap").p.get_text()
            year1=cd[:4]
            details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie URL":"","year":""}
            details["movie_rank"]=rank
            details["movie_rating"]=rating
            details["movie_name"]=movie_name
            details["movie_reviews"]=reviews
            details["movie URL"]=movie_link
            details["year"]=year1
            top_movie.append(details.copy())
        #     print(top_movie)
       
    with open("Task1.json","w")as file:
        json.dump(top_movie,file,indent=4)
    return top_movie
data=adventure_movie()
# print(data)
# pprint.pprint(adventure_movie())



	
	
	
