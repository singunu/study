from collections import deque
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    a = str(input())
    for j in a:
        graph[i].append(int(j))

visited = [[0] * N for _ in range(N)]
def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    h_cnt = 1
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < N and 0 <= dy < N:
                if not visited[dx][dy] and graph[dx][dy]:
                    h_cnt += 1
                    visited[dx][dy] = 1
                    queue.append((dx,dy))

    return h_cnt

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            result.append(bfs(i,j))
            cnt += 1

result.sort()
print(cnt)
for i in result:
    print(i)