heights = [10, 20, 30, 10]
n = len(heights)
dp = [0] * n
def frog(n):
    if n == 0:
        dp[n] = 0
        return 0
    if n == 1:
        dp[n] = abs(heights[1] - heights[0])
        return dp[n]
    jump1 = frog(n - 1) + abs(heights[n] - heights[n - 1])
    jump2 = frog(n - 2) + abs(heights[n] - heights[n - 2])
    dp[n] = min(jump1, jump2)
    return dp[n]

print(f"The frog of {n} is {frog(n - 1)}")
print(dp)
