N = int(input())
arr = list(map(int,input().split()))
dp = [[0] * 2 for _ in range(N)]
for i in range(N):
    cnt = 1
    dp[i][0] = arr[i]
    for j in range(i+1,N):
        if dp[i][0] < arr[j]:
            cnt += 1
            dp[i][0] = arr[j]
    dp[i][1] = cnt

result = 0
for i in range(N):
    if dp[i][1] > result:
        result = dp[i][1]
print(result)