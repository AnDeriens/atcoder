n, k = list(map(int, input().split()))
h = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + abs(h[i - 1] - h[i])
    for j in range(2, k + 1):
        if i - j < 1:
            break

        dp[i] = min(dp[i], abs(h[i] - h[i - j]) + dp[i - j])

print(dp[n])
