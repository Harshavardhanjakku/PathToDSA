a = [900, 945, 1110, 1230, 1235, 1245, 1340, 1700]
d = [930, 1130, 1120, 1245, 1250, 1415, 1400, 1730]
a.sort()
d.sort()
m=len(a)
n=len(d)
i=0
j=0
count=0
res=0
while i<m and j<n:
    if a[i]<d[j]:
        count+=1
        i+=1
        res=max(res,count)
    else:
        count-=1
        j+=1
print(res)