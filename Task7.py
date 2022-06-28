import json
def get_movie_list_details():
    file=open("Task5.json","r")
    var=json.load(file)
    list=[]
    for i in var:
        if i["Director"] not in list:
            list.append(i["Director"])
    dict={}
    list1=[]
    for j in list:
        i=0
        count=0
        while i<len(var):
            if j==var[i]["Director"]:
                count+=1
            i+=1
        dict.update({j:count})
    list1.append(dict)
    print(list1)
    with open("Task7.json","w") as file1:
        json.dump(list1,file1,indent=4)
get_movie_list_details()