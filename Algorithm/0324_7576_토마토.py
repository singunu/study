from collections import deque
def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))
    dc = [0, 0, -1, 1]
    dr = [1, -1, 0, 0]
    result = 0
    while queue:
        a,b = queue.popleft()

        for i in range(4):
            dx = a + dc[i]
            dy = b + dr[i]
            if dx < 0 or dy < 0 or dx >= N or dy >= M:
                continue
            if graph[dx][dy] == 0:
                graph[dx][dy] = graph[a][b]+1

                queue.append((dx,dy))

    for i in range(N):
        for j in range(M):
            if graph[i][j] > result:
                result = graph[i][j] - 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                result = -1

    return result

M, N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cnt += 1
result = bfs()
if cnt == 0:
    print(0)
else:
    print(result)