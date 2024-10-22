import json
axis_list=["function","component","company"]
element_list=["m1","m2","m3","m4","m5","m6"]
subelements_list=[["sub1","sub2"],["sub3"],["sub4","sub5","sub6"],["sub7","sub8"],["sub9","sub10"],["sub11"]]
dist={}
index=0
for i in range(len(axis_list)):
    for j in range(len(element_list)):
        for k in (subelements_list[j]):
            temp = {}
            temp["axis"]=axis_list[i]
            temp["element"]=element_list[j]
            temp["sub_element"]=k
            dist[index]=temp
            index+=1
jdict=json.dumps(dist,indent=4)
print(jdict)


