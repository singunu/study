from collections import deque


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
camera_1 = []
camera_2 = []
camera_3 = []
camera_4 = []
camera_5 = []

def bfs(a,b,cmr):
    queue = deque()
    queue.append((a,b))
    max_v = 0
    cnt = 0
    if cmr == 1:
        for i in range(0,a):
            if arr[i][b] != 6:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

        for i in range(a,N):
            if arr[i][b] != 6:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

        for j in range(0,b):
            if arr[a][j] != 6:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

        for j in range(b,M):
            if arr[a][j] != 6:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

    if cmr == 2:




result = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cmr = arr[i][j]
            result.append(bfs(i,j,cmr))
