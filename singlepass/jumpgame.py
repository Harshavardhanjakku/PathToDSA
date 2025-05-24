def canJump(nums):
    n = len(nums)
    if n == 1:
        return True
    if nums[0] == 0:
        return False

    curr = nums[0]
    for i in range(1, n):
        curr -= 1
        if curr < 0:
            return False
        curr = max(curr, nums[i])
    return True
print(canJump([2, 3, 1, 1, 4]))