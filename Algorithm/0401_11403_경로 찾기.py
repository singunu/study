from collections import deque
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
adj = [[0] * N for _ in range(N)] # 결과값 넣을 배열

def bfs(i):
    visited = [0] * N       # 출발지점(i)마다의 방문표시를 위한 배열
    queue = deque()
    queue.append(i)

    while queue:           # 큐는 i로 시작해서 계속 출발점(i)과 간선으로 연결된 도착점(j)으로 이어가기
        current = queue.popleft()

        for j in range(N):      # 연결된 간선들(j)을 돌면서
            if not visited[j] and arr[current][j]:  # 방문하지 않은 도착점만, 1일 경우만
                queue.append(j)                     # 도착지점(j)를 다시 출발지점(i)으로
                visited[j] = 1                      # 도착지점(j)에서 출발한적 있다는 표시
                adj[i][j] = 1                       # 출발점과 도착점이 연결되어 있다는 표시

for i in range(N):      # arr의 출발지점(i)을 돌면서
    bfs(i)              # 행별로 반복

for i in adj:
    print(*i)
