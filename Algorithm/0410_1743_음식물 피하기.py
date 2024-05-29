from collections import deque
N, M, K = map(int, input().split())
graph = [[-1] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for tc in range(K):
    r, c = map(int,input().split())
    r -= 1
    c -= 1
    graph[r][c] = 0

dr = [0,0,-1,1]
dc = [1,-1,0,0]
def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy] and graph[dx][dy] == 0:
                    visited[dx][dy] = 1
                    cnt += 1
                    queue.append((dx,dy))
    return cnt

result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            result.append(bfs(i,j))
print(max(result))
