def singleNonDuplicate(nums):
        i=0
        j=len(nums)-1

        while i<j:
            m=(i+j)//2  
            print(f"{i=} {m=} {j=} ")
            if (m-i+1)%2:
                j=m
            elif (j-m)%2:
                i=m+1
            else:
                  if (j-i)==2:
                    if nums[m]==nums[i]:
                            return nums[j]
                    if nums[m]==nums[j]:
                            return nums[i]
nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))