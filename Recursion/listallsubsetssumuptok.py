def subset(arr,n,ind,target,s=[]):
    if ind==n:
        if target==0:
            pass
        return 0
    if arr[ind]<=target:
       return 1+subset(arr,n,ind+1,target-arr[ind],s+[arr[ind]])
    return subset(arr,n,ind+1,target,s)
a=[2,4,6,8]
n=4
target=14
subset(a,n,0,target,[])
