# N = int(input())
# arr = list(map(int,input().split()))
# dp = [[] for _ in range(N)]
# max_v = -100000000
# for i in range(N):
#     dp[i].append(arr[i])
#     for j in range(i+1,N):
#         dp[i].append(dp[i][-1]+arr[j])
#     if max_v < max(dp[i]):
#         max_v = max(dp[i])
#
# print(max_v)

N = int(input())
arr = list(map(int,input().split()))
arr.append(-1001)
for i in range(N-1, -1, -1):
    arr[i] += max(0, arr[i+1])
print(max(arr))


