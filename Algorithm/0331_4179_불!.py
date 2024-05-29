from collections import deque
R, C = map(int,input().split())
myro = [[] * C for _ in range(R)]
for i in range(R):
    a = list(map(str,input()))
    myro.append(a)
visited = [[0]*C for _ in range(R)]
fire_visited = [[0]*C for _ in range(R)]
# print(visited)
# for i in myro:
#     print(i)


def bfs():

    visited[][] = 1
    fire_visited[][]
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]





jihun = deque()
fire = deque()


for i in range(C):
    for j in range(R):
        if myro[i][j] == 'J':
            jihun.append((i,j))
        if myro[i][j] == 'F':
            fire.append((i,j))

# 불2개, 지훈 동시에 함수 호출
# 불, 지훈 변수에 담고
# 불이 몇개일지 모르니까
# 불 변수의 len값으로 갯수만큼 함수 호출 or while문 시작
#