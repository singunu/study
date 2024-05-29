from collections import deque
N = int(input())
arr = [list(map(str,input())) for _ in range(N)]

visited_n = [[0]*N for _ in range(N)]
visited_c = [[0]*N for _ in range(N)]
cnt_n = 0
cnt_c = 0
dr = [0,0,1,-1]
dc = [1,-1,0,0]

def red(a,b):
    queue = deque()
    queue.append((a,b))
    visited_n[a][b] = 1

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            elif not visited_n[dx][dy]:
                if arr[dx][dy] == 'R':
                    visited_n[dx][dy] = 1
                    queue.append((dx,dy))


def green(a, b):
    queue = deque()
    queue.append((a, b))
    visited_n[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            elif not visited_n[dx][dy]:
                if arr[dx][dy] == 'G':
                    visited_n[dx][dy] = 1
                    queue.append((dx, dy))

def blue(a, b):
    queue = deque()
    queue.append((a, b))
    visited_n[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            elif not visited_n[dx][dy]:
                if arr[dx][dy] == 'B':
                    visited_n[dx][dy] = 1
                    queue.append((dx, dy))

def blind_red(a,b):
    queue = deque()
    queue.append((a, b))
    visited_c[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            elif not visited_c[dx][dy]:
                if arr[dx][dy] == 'R' or arr[dx][dy] == 'G':
                    visited_c[dx][dy] = 1
                    queue.append((dx, dy))


def blind_blue(a,b):
    queue = deque()
    queue.append((a, b))
    visited_c[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            elif not visited_c[dx][dy]:
                if arr[dx][dy] == 'B':
                    visited_c[dx][dy] = 1
                    queue.append((dx, dy))



for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and not visited_n[i][j]:
            red(i,j)
            cnt_n += 1
        elif arr[i][j] == 'G' and not visited_n[i][j]:
            green(i,j)
            cnt_n += 1
        elif arr[i][j] == 'B' and not visited_n[i][j]:
            blue(i,j)
            cnt_n += 1

for i in range(N):
    for j in range(N):
        if (arr[i][j] == 'R' or arr[i][j] == 'G') and not visited_c[i][j]:
            blind_red(i,j)
            cnt_c += 1
        elif arr[i][j] == 'B' and not visited_c[i][j]:
            blind_blue(i,j)
            cnt_c += 1

print(f'{cnt_n} {cnt_c}')