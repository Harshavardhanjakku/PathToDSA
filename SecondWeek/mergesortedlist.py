a=[2,4,5,8,9]
m=len(l)
b=[3,5,6,9,11,12,13]
n=len(b)
i=0
j=0
final=[]
while i<m and j<n:
    if a[i]<b[j]:
        final.append(a[i])
        i+=1
    else:
        final.append(b[j])
        j+=1
if i<m :
    while i<m:
        final.append(a[i])
        i+=1
if j<n:
    while j<n:
        final.append(b[j])
        j+=1
print(final)

