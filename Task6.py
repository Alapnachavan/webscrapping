import json
a=open("task5.json","r")
r=a.read()
movie_list=json.loads(r)
# print(movie_list)

def group_by_language():
    langu_list=[]
    dict={}
    for movie in movie_list:
        for k in movie["language"]:
            if k not in langu_list:
                langu_list.append(k)
                # print(langu_list)
    for i in langu_list:
        c=0
        for j in movie_list:
            for l in j["language"]:
                if l==i:
                    c+=1
                else:
                    pass
                dict[i]=c
    print(dict) 
    return dict   

movie_dict=group_by_language()    

with open ("task6.json","w") as f:
    a=json.dump(movie_dict,f,indent=4)  
    