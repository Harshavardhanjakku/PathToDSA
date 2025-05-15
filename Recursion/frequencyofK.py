def frequencyofK(mylist,ind,k):
    if ind==len(mylist):
        return 0
    if mylist[ind]==k:
        return 1+frequencyofK(mylist,ind+1,k)
    return frequencyofK(mylist,ind+1,k)
    
l=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
print(frequencyofK(l,0,k))