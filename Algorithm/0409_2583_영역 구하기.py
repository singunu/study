from collections import deque
M, N, K = map(int,input().split())
graph = [[0] * N for _ in range(M)]
lst = []
dr = [0,0,1,-1]
dc = [1,-1,0,0]

for tc in range(K):
    lst.append(list(map(int, input().split())))

for k in range(K):
    for i in range(lst[k][0],lst[k][2]):
        for j in range(lst[k][1],lst[k][3]):
            graph[j][i] -= 1

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 1
    area = 1
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < M and 0 <= dy < N:
                if graph[dx][dy] == 0:
                    graph[dx][dy] = graph[x][y] + 1
                    queue.append((dx,dy))
                    area += 1

    return area

cnt = 0
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            result.append(bfs(i,j))
            cnt += 1

print(cnt)
result.sort()
print(*result)