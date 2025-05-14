def checkmaxi(l,low,high):
    mid=(low+high)//2
    if low==high :
        return l[mid]
    return max(checkmaxi(l,low,mid),checkmaxi(l,mid+1,high))

l=[100,13,12,18,103,14,15,6,99]
n=len(l)
print(checkmaxi(l,0,n-1))