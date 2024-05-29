# N = int(input())
# TP = []
# for i in range(N):
#     TP.append(list(map(int,input().split())))
# result = 0
# def dfs(n,sum_p):
#     global result
#     result = max(result, sum_p)
#     if n >= N:
#         return
#     elif n + TP[n][0] <= N:
#         dfs(n+TP[n][0], sum_p+TP[n][1])
#     dfs(n+1,sum_p)
#
# dfs(0,0)
# print(result)

N = int(input())
TP = [list(map(int,input().split())) for _ in range(N)]
TP.append([0,0])
dp = [0] * (N+2)

for i in range(N-1,-1,-1):      # 앞부터 하면 이중으로 확인해야 하기 때문에 뒤부터
    if TP[i][0] + i <= N:       # 현재 일 + 소요 일이 퇴사날보다 뒤가 아닌 경우만
        dp[i] = max(dp[i+TP[i][0]] + TP[i][1], dp[i+1]) # 소요일수 뒤의 최대값+오늘값 vs 오늘 안하고 내일값
    else:
        dp[i] = dp[i+1]         # 오늘 안하고 내일 값만 그대로
print(dp[0])