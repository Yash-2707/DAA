def minCoins(coins, sum):
    n = len(coins)
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0  
    for i in range(1, sum + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[sum] == float('inf'):
        return -1
    else:
        return dp[sum]

coins = [1, 2, 5]
sum = 11
print("Minimum coins:", minCoins(coins, sum))