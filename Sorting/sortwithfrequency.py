l=[7,2,6,3,6,7,7,2,2,2]
n=10
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for i in range(n-1):
    for j in range(n-i-1):
        if dic[l[j]]>dic[l[j+1]]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)