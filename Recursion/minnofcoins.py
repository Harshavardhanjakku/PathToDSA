def mincoins(arr, n, ind, target):
    if target == 0:
        return 0
    if ind == n or target < 0:
        return float('inf')

    take = 1 + mincoins(arr, n, ind + 1, target - arr[ind])
    skip = mincoins(arr, n, ind + 1, target)

    return min(take, skip)

arr = [1, 2, 3, 4]
n = len(arr)
target = 5
res = mincoins(arr, n, 0, target)
print(res if res != float('inf') else -1)
