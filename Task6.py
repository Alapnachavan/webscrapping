import json
def scrap_movie_details():
    file=open("Task5.json","r")
    var=json.load(file)
    # print(var)
    list=[]
    for i in var:
        if i["Original Language"] not in list:
            list.append(i["Original Language"])
            # print(list)
        dict={}
        list1=[]
        for k in list:
            i=0
            count=0
            while i<len(var):
                if k==var[i]["Original Language"]:
                    count=count+1
                i=i+1
            dict.update({k:count})
        list1.append(dict)
        with open("Task6.json","w") as file1:
            json.dump(dict,file1,indent=4)
    return list1
list1=scrap_movie_details()