heights = [10, 20, 30, 10]
n = len(heights)
dp = [0] * n
dp[0] = 0
dp[1] = abs(heights[1] - heights[0])
k=3
for i in range(2, n):
    mini = float('inf')
    for jump in range(1, k + 1):
        if i - jump >= 0:
            cost = dp[i - jump] + abs(heights[i] - heights[i - jump])
            if cost < mini:
                mini = cost
    dp[i] = mini
print(dp)
