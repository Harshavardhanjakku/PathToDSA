def countmaxone(nums):
    n=len(nums)
    left=right=0
    mymaxi=0
    for i in range(n):
        if nums[i]==0:
            left=right+1
        mymaxi=max(mymaxi,right-left+1)
        right+=1
    return mymaxi
nums=[1,1,0,1,1,1]
print(countmaxone(nums))
