import json
element_list=["m1","m2","m3"]
subelements_list=[["sub1","sub2"],["sub3"],["sub4","sub5","sub6"]]
dict={}
t = 0
for i in range(len(element_list)):
    for j in range(len(subelements_list[i])):
        sub = {}
        sub["element"] = element_list[i]
        sub["sub_element"]= subelements_list[i][j]
        dict[t] = sub
        t+=1
print(dict)
result=json.dumps(dict,indent=4)
print(result)
