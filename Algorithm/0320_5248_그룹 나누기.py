
# def solve(v):
#     a = [v]
#     visited[v] = 1
#     while a:
#         now = a[-1]
#         for i in range(N+1):
#             if visited[now][i] == 1 and
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     graph = [[0] * (N + 1) for _ in range(N + 1)]
#     arr = list(map(int,input().split()))
#     visited = [0] * (N + 1)
#     for i in range(0, M*2, 2):
#         graph[arr[i]].append(arr[i+1])
#         graph[arr[i+1]].append(arr[i])
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if visited[i] == 0:
#             solve(i)
#             cnt += 1
#
#     print(f'#{tc} {cnt}')


def find_set(x):
    if p[x] == x:
        return x
    while p[x] != x:
        x = p[x]                    # 같은 조로 표시하기 위해
    return x                        # 뒷값(대표값)으로 변경 및 통일하기 위한 값을 반환

def union(x,y):
    r1 = find_set(x)
    r2 = find_set(y)
    p[r1] = r2                      # 받은 x값을 인덱스로 하여 앞값을 뒷값(대표값)으로 변경

def solve():
    for i in range(0,M*2,2):
        union(data[i], data[i+1])   # 조 호출
        # print(f'p {p}')
    r_set = []
    for i in range(1,N+1):
        r_set.append(find_set(i))      # 중복없이 추가
        # print(f'r_set {r_set}')
    return (r_set)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    p = [x for x in range(N+1)]     # 0부터 N까지 숫자배열 생성
    # print(p)
    result = solve()
    print(f'#{tc} {result}')