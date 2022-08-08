  
from pprint import pprint
import json
a=open("Movies_Detail.json","r")
r=a.read()
movie_list=json.loads(r)


def group_by_year():
    year_list=[]
    dict={}
    for movie in movie_list:
        year=movie["year_of_release"]
        movie_list2=[]
        # print(movie)
        # print(year)
        if year not in year_list:
            year_list.append(year)
            year_list.sort()
            print(year_list)
            for movie1 in movie_list:
                if movie1["year_of_release"]==year:
                    movie_list2.append(movie1)
                    # pprint(movie_list2)
                else:
                    pass
            dict[year]=movie_list2
    pprint(dict) 
    return dict   

movie_dict=group_by_year()    

with open ("task2.json","w") as f:
    a=json.dump(movie_dict,f,indent=4)  