N = int(input())
m = int(input())
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []
for i in range(m):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(x,lv):
    if lv == 2:
        return
    visited[x] = 1
    for i in lst[x]:
        if not visited[i]:
            dfs(i,lv+1)
            if i not in result:
                result.append(i)

dfs(1,0)
print(len(result))