from collections import deque

def bfs(V):
    queue = deque([V])                              # q는 1
    visited_bfs[V] = 1                              # 방문한 인덱스를 체크
    while queue:                                    # queue가 다 없어질 때까지 반복
        V = queue.popleft()                         # queue의 0번자리를 V로 받아오며 while문이 끝나게 하려고 queue의 값은 지우기
        print(V, end=' ')                           # 출력

        for i in range(1, N + 1):                   # graph를 for로 1열씩 열 먼저 다돌고 다음 while로 돌아가기
            # print(V,i, visited_bfs[i], graph[V][i])
            if visited_bfs[i] == 0 and graph[V][i]:   # 미방문 인덱스, 간선 있는 값일 경우
                queue.append(i)                     # 나중에 순서가 오면 while로 돌 queue에 저장
                visited_bfs[i] = 1                  # 방문한 인덱스 체크


def dfs(V):
    visited_dfs[V] = 1                                  # 함수 호출마다 방문 체크
    print(V, end=' ')                               # 방문한 그래프 인덱스자리의 데이터값 출력
                                                    # 왜냐하면 인덱스로 출발하여 값으로 이동
    for i in range(1, N + 1):
        # print(V,i,visited_dfs,graph[V][i])
        if visited_dfs[i] == 0 and graph[V][i]:           # 방문 안된 인덱스, 간선있는 노드로
            dfs(i)                                  # 깊이 우선이니까 i(값)을 인덱스로 호출


N, M, V = map(int,input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]       # 간선 정보를 저장할 그래프 0빼고 1부터라서 N+1만큼 생성
visited_dfs = [0] * (N + 1)                             # 방문했던 인덱스를 다시 가지 않기위해 체크 배열 생성
visited_bfs = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())                # 인풋값을 for문으로 돌면서 받으면서
    graph[a][b] = 1                                 # 무향 그래프의 간선정보를 양쪽 인덱스에 저장
    graph[b][a] = 1

dfs(V)
print()
bfs(V)

