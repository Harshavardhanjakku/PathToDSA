l=[2,13,4,2,9,9,5,8,7,13,3]
c=0
maxele=l[0]
for i in l:
    if i>maxele:
        maxele=i
    c+=1
checklist=[0]*(maxele+1)
for i in l:
    checklist[i]+=1
print(checklist)
k=3
flagcount=0
for i in range(maxele,-1,-1):
    if checklist[i]==1:
        flagcount+=checklist[i]
    if flagcount==k:
        print(i)
        break