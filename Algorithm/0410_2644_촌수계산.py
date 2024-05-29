n = int(input())
a,b = map(int,input().split())
m = int(input())
visited = [0] * (n+1)
lst = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)
result_cnt = -1
def dfs(x,cnt):
    global result_cnt
    visited[x] = 1
    if x == b:
        result_cnt = cnt
        return

    for i in lst[x]:
        if not visited[i]:
            dfs(i,cnt+1)

dfs(a,0)
print(result_cnt)
