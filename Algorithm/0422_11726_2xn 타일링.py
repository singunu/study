N = int(input())
if N > 3:
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N] % 10007)
elif N == 1:
    print(1)
elif N == 2:
    print(2)
elif N == 3:
    print(3)
