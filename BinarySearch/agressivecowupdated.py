def check(a,mind,nofcow):
    i=a[0]
    nofcow=nofcow-1
    curr=a[0]
    for i in range(1,len(a)):
        if a[i]-curr>=mind:
            curr=a[i]
            nofcow-=1
    return nofcow<=0
def binary(a,nofcow):
    low=1
    high=max(a)-min(a)
    res=1
    while low<=high:
        mid=(low+high)//2
        if check(a,mid,nofcow):
            res=mid
            low=mid+1
        else:
            high=mid-1
    return res

a=[1,2,5,7,10]
nofcow=3
print(binary(a,nofcow))