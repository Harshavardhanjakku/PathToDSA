
def generatesubsets(arr,n,ind,mylist,target):
    if ind==n:
        return sum(mylist)==target
    return generatesubsets(arr,n,ind+1,mylist,target) or generatesubsets(arr,n,ind+1,mylist+[arr[ind]],target)
print(generatesubsets([2,3,4],3,0,[],7))

