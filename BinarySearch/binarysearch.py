def binarysearch(nums,target):
    low=0
    high=len(nums)-1
    while low <= high :
        mid=(low)+(high-low)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        return -1
nums=[1,2,3,3,3,8,9]
target=3
print(binarysearch(nums,target))