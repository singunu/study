from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if graph[dx][dy]:
                queue.append((dx, dy))
                graph[dx][dy] = 0
                cnt += 1
    return cnt
result = []
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            result.append(bfs(graph,i,j))

if not len(result):
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))