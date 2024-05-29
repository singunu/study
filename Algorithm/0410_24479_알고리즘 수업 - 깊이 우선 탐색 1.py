import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()

cnt = 1
def dfs(r):
    global cnt
    visited[r] = cnt

    for i in arr[r]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(R)
for i in range(1,N+1):
    print(visited[i])
# cnt = 1
# stack = deque()
# stack.append(R)
# while stack:
#     x = stack.pop()
#     visited[x] = cnt
#     cnt += 1
#
#     for i in arr[x]:
#         if not visited[i]:
#             stack.append(i)
#
#              visited[i] = cnt

