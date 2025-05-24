import math

def check(l,h,k):
    counthours=0
    for i in l:
        counthours+=math.ceil(i/k)
    return counthours
def binarysearch(l,h):
    low=1
    high=max(l)
    res=1
    while low<=high:
        mid=(low+high)//2
        if check(l,h,mid)<h:
            high=mid-1
        elif check(l,h,mid)>h:
            low=mid+1
        else:
            return mid
l=[3,6,7,11]
h=8
print(binarysearch(l,h))