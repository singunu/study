T = int(input())
arr = [int(input()) for _ in range(T * 2)]
dp = [[0] * 15 for _ in range(15)]

for i in range(15):
    for j in range(15):
        if i == 0:
            dp[0][j] += j
        for k in range(1, j + 1):
            dp[i][j] += dp[i-1][k]

for i in range(0,T * 2, 2):
    print(dp[arr[i]][arr[i+1]])

