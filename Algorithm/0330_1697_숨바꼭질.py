from collections import deque
N, K = map(int,input().split())
max_v = 10**5 + 1
visited = [0] * max_v
def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        a = queue.popleft()
        if a == K:
            return visited[a]
        for i in (a+1, a-1, a*2):
            if 0 <= i < max_v and not visited[i]:
                visited[i] = visited[a] + 1
                queue.append(i)

print(bfs())