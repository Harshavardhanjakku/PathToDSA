l=[2,13,13,13,4,2,9,9,4,5,8,8,8,7,13,3]
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
myfrequency=0
myvalue=None
for i in dic:
    if dic[i]>myfrequency:
        myfrequency=dic[i]
        myvalue=i
print(myvalue)

