import json
a=open("task5.json","r")
r=a.read()
movie_list=json.loads(r)
# print(movie_list)


    
def group_by_director():
    langu_list=[]
    dict={}
    for movie in movie_list:
        s=""
        for k in movie["Director"]:
            s+=k
        if s not in langu_list:
            langu_list.append(s)
            # print(langu_list)
    for i in langu_list:
        c=0
        for j in movie_list:
            s2=""
            for l in j["Director"]:
                s2+=l
            if s2==i:
                c+=1
            else:
                pass
            dict[i]=c
    # print(dict) 
    return dict   

movie_dict=group_by_director()    

with open ("task7.json","w") as f:
    a=json.dump(movie_dict,f,indent=4)    