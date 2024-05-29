def dfs(idx,cnt):
    visited[idx] = 1
    for i in arr[idx]:
        if not visited[i]:
            cnt = dfs(i,cnt+1)
    return cnt

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    arr = [[] for _ in range(N+1)]
    visited = [0] * (N + 1)
    visited[0] = 1
    for i in range(M):
        a, b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)

    print(dfs(1,0))

