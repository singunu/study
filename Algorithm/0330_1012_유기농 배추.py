from collections import deque
def dfs(a,b):
    queue = deque()
    queue.append((a,b))
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy] and data[dx][dy]:
                    visited[dx][dy] = 1
                    queue.append((dx,dy))


T = int(input())
cnt_lst = []
for tc in range(T):
    arr = []
    cnt = 0
    M,N,K = map(int,input().split())
    visited = [[0] * M for _ in range(N)]
    data = [[0] * M for _ in range(N)]

    for i in range(K):
        a,b = map(int,input().split())
        arr.append(a)
        arr.append(b)

    for i in range(0,(K*2),2):
        data[arr[i+1]][arr[i]] = 1

    for i in range(N):
        for j in range(M):
            if data[i][j] and not visited[i][j]:
                visited[i][j] = 1
                dfs(i,j)
                cnt += 1
    cnt_lst.append(cnt)
    cnt = 0

for i in cnt_lst:
    print(i)
# 출력값 받아오기
# bfs 호출
# 호출 될 때마다 카운트, 방문표시(함수안에)
# dc,dr
# 큐에 초기값 받아오기
# 와일문안에 큐 팝레프트
#