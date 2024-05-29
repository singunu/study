from collections import deque
import copy

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
result = 0
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def bfs():
    global result
    queue = deque()
    lab = copy.deepcopy(graph)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if 0 <= dx < N and 0 <= dy < M:
                if not lab[dx][dy]:
                    lab[dx][dy] = 2
                    queue.append((dx,dy))

    for i in range(N):
        for j in range(M):
            if not lab[i][j]:
                cnt += 1

    result = max(cnt, result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0

wall(0)
print(result)