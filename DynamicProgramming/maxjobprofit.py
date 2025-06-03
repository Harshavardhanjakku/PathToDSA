times = [(1, 2), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
profit = [5, 6, 5, 4, 11, 2]
n = len(times)

def iscompatible(i, j):
    return times[i][1] <= times[j][0]

memo = {}

def getprofit(index):
    if index >= n:
        return 0
    if index in memo:
        return memo[index]
    include = profit[index]
    nextindex = index + 1
    while nextindex < n and not iscompatible(index, nextindex):
        nextindex += 1
    include += getprofit(nextindex)
    exclude = getprofit(index + 1)
    memo[index] = max(include, exclude)
    return memo[index]

print("Maximum Profit:", getprofit(0))
