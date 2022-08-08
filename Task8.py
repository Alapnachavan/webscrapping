from Task1 import top_movies
from Task4 import scrap
import json
import os
from bs4 import BeautifulSoup

url=top_movies[1]["link"]

def movie_details(movie_detail):
    movie_id=""
    for id in movie_detail[27:-1]:
        movie_id+=id
        # print(movie_id)
    filename=movie_id+'.json'
    text=os.path.exists(filename)
    if text==True:
        with open(filename,"r")as f:
            a=json.load(f)    
        print(a)   
    else:
        data=scrap(url) 
        with open(filename,"w") as f:
            json.dump(data,f,indent=6)
        # print(data)  
          
movie_details(url)        