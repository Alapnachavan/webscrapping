import json
a=open("task5.json","r")
r=a.read()
movie_list=json.loads(r)
# print(movie_list)

def analisis_by_director_language(movie_list):
    director_dic={}
    for movie in movie_list:
        director=movie["Director"]
        director_dic[director]={}
        count=0
        for i in range(len(movie_list)):
            if director==movie_list[i]["Director"]:
                language=movie_list[i]["language"]
                count+=1
                for l in language:
                    director_dic[director].update({l:count})
    with open("task10.json","w") as f:
        json.dump(director_dic,f,indent=6)
    print(director_dic)
          
       
analisis_by_director_language(movie_list)   