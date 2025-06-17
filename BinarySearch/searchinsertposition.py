def linearsearch(nums,target):
    for ind,ele in enumerate(nums):
        if target<ele:
            return ind
    return ind+1
def binarysearch(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low)+(high-low)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return low
nums=[1,3,5,8]
target=10
print(linearsearch(nums,target))
print(binarysearch(nums,target))