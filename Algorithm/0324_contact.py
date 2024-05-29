from collections import deque
def bfs(s):
    queue = deque()
    queue.append((s))
    visited = [0] * 101
    visited[s] = 1
    max_num = s
    max_depth = 1

    while queue:
        current = queue.popleft()
        for i in range(len(graph[current])):
            if visited[graph[current][i]]:
                continue

            visited[graph[current][i]] = visited[current] + 1

            if visited[graph[current][i]] > max_depth or (graph[current][i] > max_num and visited[graph[current][i]] == max_depth):
                max_num = graph[current][i]
                max_depth = visited[graph[current][i]]

            queue.append(graph[current][i])
    return max_num

T = 10
for tc in range(1, 11):
    N, S = map(int, input().split())
    data = list(map(int,input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        graph[data[i]].append(data[i+1])
    result = bfs(S)
    print(f'#{tc} {result}')