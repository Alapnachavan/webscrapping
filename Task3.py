from Task2 import movie_dict
from pprint import pprint
import json
def group_by_decade():
    
    moviedec={}
    list1=[]
    for i in movie_dict:
        # print(i)
        i=int(i)
        mode=i%10
        # print(mode)
        decade=i-mode
        # print(decade)
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    # pprint(list1)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        # print(i)
        dec10=i+9
        # print(dec10)
        for x in movie_dict:
            x=(x)
            # print(x)
            if x<=dec10 and x>=i:
                # print(x)
                for v in movie_dict[x]:
                    # pprint(v)
                    moviedec[i].append(v)

    pprint(moviedec)

    with open("task3.json","w") as a:

        json.dump(moviedec, a,indent=6)

    return moviedec


decade=group_by_decade()
