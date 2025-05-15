
def generatesubsets(arr,n,ind,target):
    if ind==n:
        return target==0
    take=False
    if arr[ind]<=target:
        take=generatesubsets(arr,n,ind+1,target-arr[ind])
    notake=generatesubsets(arr,n,ind+1,target) 
    return take or notake
arr=[1,2,3,4]
n=4
target=5
ind=0
print(generatesubsets(arr,n,ind,target))


