from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
game_board = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        if j + game_board[i][j] < N:
            dp[i][j + game_board[i][j]] += dp[i][j]

        if i + game_board[i][j] < N:
            dp[i + game_board[i][j]][j] += dp[i][j]
# def bfs():
#     global cnt
#     queue = deque()
#     queue.append((0,0))
#     while queue:
#         x,y = queue.popleft()
#         for d in range(2):
#             dx = x + game_board[x][y] * dr[d]
#             dy = y + game_board[x][y] * dc[d]
#             if dx >= N or dy >= N:
#                 continue
#             if not game_board[dx][dy]:
#                 cnt += 1
#             if game_board[dx][dy]:
#                 queue.append((dx,dy))
#     return
#
# bfs()
# print(cnt)

