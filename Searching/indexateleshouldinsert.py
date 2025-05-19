def binarysearch(l,ele):
    low=0
    high=len(l)-1
    while low<=high:
        mid=low+(high-low)//2
        if l[mid]==ele:
            return mid
        if l[mid]>ele:
            high=mid-1
        else :
            low=mid+1 
    else:
        return low

l=[2,3,5,6,7,7,8,9,10,10,10,13,15]
print(binarysearch(l,9))