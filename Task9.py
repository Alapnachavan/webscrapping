from Task1 import top_movies
from Task4 import scrap
import json
import os
import random,time

def movie_details(movie_detail):
    i=0
    while i<10:
        url=movie_detail[i]["link"]
        random_sleep=random.randint(1,2)
        movie_id=""
        for id in url[27:-1]:
            movie_id+=id
        # print(movie_id)
        filename=movie_id+'.json'
        text=os.path.exists(filename)
        if text==True:
            with open(filename,"r")as f:
                a=json.load(f)    
            print(a)   
        else:
            time.sleep(random_sleep)
            data=scrap(url) 
            with open(filename,"w") as f:
                json.dump(data,f,indent=6)
        i=i+1  
          
movie_details(top_movies)        


