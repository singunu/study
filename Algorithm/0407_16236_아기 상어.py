from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]


'''
먹으러가는 시간동안 생존
if 이동이면 그대로
if 먹기면 if 
같은 거리에서 1마리라면 그 물고기
1마리보다 많다면 가장가까운 물고기
다 거리가 같다면 1. 위 2. 왼쪽
지나갈수도 먹을수도

상하좌우 돌면서 다 나보다 클 경우 종료
0일 경우 



bfs들어와서 queue에 넣고 while 시작
x,y 따오고
for문으로 상하좌우 dx,dy 탐색
크기가 나보다 낮으면 먹기
같으면 위부터
'''

dr = [0,0,-1,1]
dc = [1,-1,0,0]


def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    size = 2
    cnt = 0
    while queue:
        x, y = queue.popleft()
        adj = []
        for d in range(4):
            dx = x + dr[d]
            dy = y + dc[d]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            if graph[dx][dy] > size:
                continue
            if graph[dx][dy] < size:
                queue.append((dx,dy))
                graph[dx][dy] = 0
                cnt += 1
                if cnt == size:
                    size += 1
            elif graph[dx][dy] == size:
                queue.append((dx,dy))
                cnt += 1


queue = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            queue.append((i,j))

i,j = queue.popleft()
bfs(i,j)