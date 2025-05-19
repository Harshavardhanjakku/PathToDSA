l=[2,1,1,2,1,1,1]
dic={}
count=0
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
    count+=1
print(dic)
for i in dic:
    if dic[i]>count//2:
        print(i)
        break

