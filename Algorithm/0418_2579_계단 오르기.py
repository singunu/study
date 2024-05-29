
N = int(input())
stairs = [0]
for i in range(N):
    stairs.append(int(input()))
dp = [[0] * 3 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(3):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i-1][0] + stairs[i]
        dp[i][2] = dp[i-1][1] + stairs[i]
print(max(dp[N][1], dp[N][2]))


