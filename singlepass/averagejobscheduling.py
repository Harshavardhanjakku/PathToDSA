l=[4,3,7,1,2,6]
l.sort()
n=len(l)
tot=0
findtot=0
for i in range(1,n):
    tot+=l[i-1]
    findtot+=tot
print(findtot)