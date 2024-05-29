from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dr = [0,0,-1,1]
dc = [1,-1,0,0]
year = 0
piece_cnt = 0
def iceburg():
    melting_lst = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            cnt = 0
            if graph[i][j] > 0:
                for d in range(4):
                    di = i + dr[d]
                    dj = j + dc[d]
                    if 0 <= di < N and 0 <= dj < M:
                        if graph[di][dj] <= 0:
                            cnt += 1
                melting_lst[i][j] += cnt

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                graph[i][j] -= melting_lst[i][j]


def piece_check(a,b):
    visited[a][b] = 1
    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy] and graph[dx][dy] > 0:
                    visited[dx][dy] = 1
                    queue.append((dx,dy))

while True:
    for i in graph:
        print(i)
    print('-------------')
    if piece_cnt >= 2:
        print(year)
        break

    iceburg()
    piece_cnt = 0
    year += 1
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                piece_check(i,j)
                piece_cnt += 1

    if not piece_cnt:
        print(0)
        break

