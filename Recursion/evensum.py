def evensum(mylist,ind):
    n=len(mylist)
    if ind==n:
        return 0
    if  mylist[ind]%2==0:
       return mylist[ind]+evensum(mylist,ind+1)
    return evensum(mylist,ind+1)
a=[2,5,6,7,2,1,4,3,6]
print(evensum(a,0))
