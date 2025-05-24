def checksum(l,x):
    i=0
    n=len(l)
    j=n-1
    while i<n and j>=0:
        if l[i]+l[j]==target:
            return (l[i],l[j])
        elif l[i]+l[j]<target:
            i+=1
        else:
            j-=1
    else:
        return -1
l=[3,2,4]
target=6
print(checksum(l,target))