coins = [2, 3, 4, 5]
targetamt = 13

dp = [[0] * (targetamt + 10) for _ in range(len(coins))]
for i in range(len(coins)):
    dp[i][0] = 1
if coins[0] <= targetamt:
    dp[0][coins[0]] = 1
for i in range(1, len(coins)):
    for j in range(1, targetamt + 1):
        if j < coins[i]:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j] or dp[i-1][j - coins[i]]:
                dp[i][j] = 1
for i in dp:
    print(i)
print("\nTarget achievable:", bool(dp[-1][targetamt]))
