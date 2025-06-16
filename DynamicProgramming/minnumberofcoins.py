coins = [2, 3, 4, 5]
targetamt = 13

INF = float('inf')
dp = [[INF] * (targetamt + 1) for _ in range(len(coins))]

for i in range(len(coins)):
    dp[i][0] = 0
for j in range(targetamt + 1):
    if j % coins[0] == 0:
        dp[0][j] = j // coins[0]
for i in range(1, len(coins)):
    for j in range(1, targetamt + 1):
        if j < coins[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - coins[i]])
for row in dp:
    print(row)
if dp[-1][targetamt] == INF:
    print("\nTarget not achievable.")
else:
    print("\nMinimum coins required to reach target:", dp[-1][targetamt])
