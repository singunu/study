from collections import deque

def bfs(a,b):
    visited[a][b] = 1
    queue = deque()
    queue.append((a,b))
    dr = [0,0,1,-1,1,-1,1,-1]
    dc = [1,-1,0,0,1,-1,-1,1]

    while queue:
        x,y = queue.popleft()
        for d in range(8):
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < h and 0 <= dy < w:
                if not visited[dx][dy] and graph[dx][dy]:
                    visited[dx][dy] = 1
                    queue.append((dx,dy))

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)