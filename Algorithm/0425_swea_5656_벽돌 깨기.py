
# '''
# t동안
# 모든 경우의수 맨위에있는거 다돌아보기 -> 함수 호출
# 함수 들어왔으면 그거 터트리고 연쇄작용 다한다음 N-1번 더
# 구슬 던지기를 N번 dfs에서 하고 맥스값을 리턴
# 구슬던지기 한번에 터지는 연쇄작용을 bfs안에서 적용
# 연쇄작용은 한번에 되어야 하므로 체크해두었다가 뱅
# visited 어떻게 할지 -> dfs에서 모든 경우의수를 볼때 비짓티드
#
#
# 비짓티드, 어레이 초기화 시점
# 1. 함수 들어가기 전 매 j 돌릴떄마다
# 2. 함수 들어가서 bfs돌리고 다음꺼 나머지 N-1개 돌리는거에서 bfs 1번 완료한 그걸로 다시
#
# '''
# dr = [0,0,-1,1]
# dc = [1,-1,0,0]
#
# def dfs(a,b,lst,n):
#     if n > N:
#         cnt = 0
#         for i in range(H):
#             for j in range(W):
#                 if lst[i][j] > 0:
#                     cnt += 1
#         dfs_result.append(cnt)
#         return
#
#     bfs(a,b)
#
#     for i in range(H):
#         for j in range(W):
#             if not visited_dfs[i][j]:
#                 visited_dfs[i][j] = 1
#                 dfs(i, j, lst, n+1)
#
# def bfs(q,w):
#     queue = []
#     queue.append(q)
#     queue.append(w)
#     check = [[0] * W for _ in range(H)]
#     bang = [[0] * W for _ in range(H)]
#     check[q][w] = 1
#     while queue:
#         y = queue.pop()
#         x = queue.pop()
#         for num in range(1, new_arr[x][y]):
#             for d in range(4):
#                 dx = x + (dr[d] * num)
#                 dy = y + (dc[d] * num)
#                 if dx < 0 or dx >= H or dy < 0 or dy >= W:
#                     continue
#                 if new_arr[dx][dy] <= 0:
#                     continue
#                 if new_arr[dx][dy] > 1 and not check[dx][dy]:
#                     queue.append(dx)
#                     queue.append(dy)
#                     check[dx][dy] = 1
#                 if new_arr[dx][dy] == 1 and not check[dx][dy]:
#                     check[dx][dy] = 1
#     for i in range(H):
#         for j in range(W):
#             if check[i][j]:
#                 new_arr[i][j] = 0
#
#     for i in range(W):
#         downing = []
#         for j in range(H):
#             if new_arr[j][i]:
#                 downing.append(new_arr[j][i])
#         for k in range(H-1, H-len(downing)+1,-1):
#             new_arr[k][i] = downing.pop()
#         # for a in new_arr:
#         #     print(a)
#         # print('-------------------')
#
# T = int(input())
# for tc in range(1,T+1):
#     N,W,H = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(H)]
#     cnt = 15 * 12
#     result = []
#     visited = [[0] * W for _ in range(H)]
#     for i in range(H):
#         for j in range(W):
#             new_arr = deepcopy(arr)
#             dfs_result = []
#             visited_dfs = [[0] * W for _ in range(H)]
#             if i == 0 and not visited[i][j] and new_arr[i][j]:
#                 (dfs(i,j,new_arr,0))
#                 result.append(dfs_result)
#             elif i > 0 and new_arr[i][j] > 0 and not visited[i][j] and not new_arr[i-1][j]:
#                 (dfs(i,j,new_arr,0))
#                 result.append(dfs_result)
#
#     min_v = 15 * 12 + 1
#     for i in result:
#         if min(i) < min_v:
#             min_v = min(i)
#
#     print(f'#{tc} {min_v}')










'''
함수 내에서 인자 cnt가 N되면 리턴
상하좌우
맨 위에 있는 것만 가능하게 따오기
dfs


'''

from collections import deque

def dfs(a,b,cnt,arr):

    if cnt > N:
        result_cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    result_cnt += 1
        result_lst.append(result_cnt)
        return

    check_lst = deque()
    check_lst.append((a,b))
    visited = [[0] * W for _ in range(H)]

    while check_lst:
        x, y = check_lst.popleft()
        visited[x][y] = 1
        for d in range(4):
            for v in range(1,arr[x][y]):
                dx = x + dr[d] * v
                dy = y + dc[d] * v
                if 0 <= dx < H and 0 <= dy < W:
                    if arr[dx][dy] and not visited[dx][dy]:
                        check_lst.append((dx,dy))
                        visited[dx][dy] = 1

    for i in range(H):
        for j in range(W):
            if visited[i][j]:
                arr[i][j] = 0

    for j in range(W):
        for i in range(H-1,-1,-1):
            if not arr[i][j]:
                for ri in range(i-1,-1,-1):
                    if arr[ri][j]:
                        arr[i][j], arr[ri][j] = arr[ri][j], 0
                        break

    copy_arr = [s[:] for s in arr]

    for i in range(H):
        for j in range(W):
            if i == 0 and copy_arr[i][j]:
                dfs(i, j, cnt + 1, copy_arr)
                copy_arr = [s[:] for s in arr]
            elif i > 0 and not copy_arr[i - 1][j] and copy_arr[i][j]:
                dfs(i,j,cnt+1,copy_arr)
                copy_arr = [s[:] for s in arr]
    empty = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                empty += 1

    if not empty:
        result_lst.append(0)
        return

dr = [0,0,-1,1]
dc = [1,-1,0,0]
T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(H)]
    result_lst = deque()
    copy_graph = [s[:] for s in graph]

    for i in range(H):
        for j in range(W):
            if i == 0 and copy_graph[i][j]:
                dfs(i, j, 1, copy_graph)
                copy_graph = [s[:] for s in graph]
            elif i > 0 and not copy_graph[i - 1][j] and copy_graph[i][j]:
                dfs(i,j,1,copy_graph)
                copy_graph = [s[:] for s in graph]

    print(f'#{tc} {min(result_lst)}')