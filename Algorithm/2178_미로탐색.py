from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if not graph[dx][dy]:
                continue
            if graph[dx][dy] == 1:
                graph[dx][dy] = graph[x][y] + 1
                queue.append((dx,dy))

    return graph[N-1][M-1]
print(bfs(0,0))
'''

'''



















