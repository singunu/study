# -1뜨면 인풋 종료
# 회원번호를 인덱스로 배열 생성
# 연결문제
# dfs 인자를 점수로 하는데 오름차순
#
from collections import deque
N = int(input())
lst = [[] for _ in range(N+1)]
while True:
    a, b = map(int,input().split())
    if a == -1:
        break
    lst[a].append(b)
    lst[b].append(a)

def bfs(x):
    visited = [-1] * (N + 1)
    queue = deque()
    queue.append(x)
    visited[x] = 0
    while queue:
        a = queue.popleft()
        for i in lst[a]:
            if visited[i] == -1:
                visited[i] = visited[a] + 1
                queue.append(i)
    return max(visited)

min_lv = 50
person = []
for i in range(1,N+1):
    lv = bfs(i)
    if lv < min_lv:
        min_lv = lv
        person = [i]
    elif lv == min_lv:
        person.append(i)
print(min_lv, len(person))
person.sort()
for i in person:
    print(i, end=' ')