def binarysearch(a,x):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            return True
        elif a[mid]<x:
            low=mid+1
        else:
            high=mid-1
    else:
        return False

def findele(m,x):
    flag=False
    for i in m:
        if binarysearch(i,x):
            flag=True
    return flag
m=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
print(findele(m,14))