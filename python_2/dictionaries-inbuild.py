#dictionaries in python
dict={
    'name':'sai',
    'age':'89',
    'city':'Nellore'
    }

print(dict['age'])

dict_list=[{'name':'sai','age':69,'city':'ap'},{'name':'kamal','age':89,'city':"in"}]

for i in range(len(dict_list)):
    print(dict_list[i]['name'])

#adding elements to set
dic={}
ran=(1,4,4,3,3,5,5,6,3)
for i in ran:
    key= "count_"+str(i)
    if key in dic:
        dic[key]+=i
    else:
        dic[key]=i
print(dic)