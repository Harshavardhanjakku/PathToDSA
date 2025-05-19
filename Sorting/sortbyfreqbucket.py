a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)