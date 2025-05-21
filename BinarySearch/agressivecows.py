a=[1,2,5,7,10]
mind=3
nofcow=3
i=a[0]
nofcow=nofcow-1
curr=a[0]
for i in range(1,len(a)):
    if a[i]-curr>=mind:
        curr=a[i]
        nofcow-=1
print(nofcow==0)
