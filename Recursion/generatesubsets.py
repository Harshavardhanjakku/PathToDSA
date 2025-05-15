def generatesubsets(arr,n,ind,mylist):
    if ind==n:
        return [mylist]
    without=generatesubsets(arr,n,ind+1,mylist)
    took=generatesubsets(arr,n,ind+1,mylist+[arr[ind]])
    return without+took
    
print(generatesubsets([2,3,4],3,0,[]))