from collections import deque
def knight():
    if q == e and w == r:
        print(0)
        return
    queue = deque()
    queue.append((q,w))
    while queue:
        x,y = queue.popleft()
        for d in range(8):
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < I and 0 <= dy < I:
                if not visited[dx][dy]:
                    visited[dx][dy] = visited[x][y] + 1
                    queue.append((dx,dy))
                    if chess_board[dx][dy] == 2:
                        print(visited[dx][dy])
                        return

T = int(input())
for tc in range(T):
    I = int(input())
    chess_board = [[0] * I for _ in range(I)]
    visited = [[0] * I for _ in range(I)]
    q, w = map(int, input().split())
    e, r = map(int, input().split())
    chess_board[q][w] = 10
    chess_board[e][r] = 2
    dr = [2, 1, 2, 1, -1, -2, -2, -1]
    dc = [1, 2, -1, -2, 2, 1, -1, -2]
    knight()