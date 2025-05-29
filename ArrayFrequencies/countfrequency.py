l=[1,1,1,1,5,5,5,3,3,3,3,2,2,2]
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)