l=[2,3,4,3,3,4,5,6,7,9,2,4]
dic={}
newlist=[]
for i in l:
    if i not in dic:
        dic[i]=1
        newlist.append(i)
    else:
        dic[i]+=1
print(newlist)
# Time complexity   : O(N)
# Space Complexity  : O(N)
mydic={"1":1,"1":1}
print(mydic)
print(id(l[0]),id(l[-2]))