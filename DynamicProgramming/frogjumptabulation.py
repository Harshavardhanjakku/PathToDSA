heights = [10, 20, 30, 10]
n = len(heights)
dp = [0] * (n)

dp[1]=abs(heights[1] - heights[0])
for i in range(2,n):
    jump1 = dp[i-1] + abs(heights[i] - heights[i - 1])
    jump2 = dp[i-2] + abs(heights[i] - heights[i - 2])
    dp[i] = min(jump1, jump2)
print(dp)
