
def generatesubsets(arr,n,ind,mylist,target):
    if ind==n:
        if sum(mylist)==target:
            print(mylist)
        return sum(mylist)==target
    return generatesubsets(arr,n,ind+1,mylist,target) + generatesubsets(arr,n,ind+1,mylist+[arr[ind]],target)
print(generatesubsets([1,2,3,4],4,0,[],5))

