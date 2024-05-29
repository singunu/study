'''
정하고
이동
+1
대각보고 대각만큼 +1
나머지 2이상을 보고 -2

이동
+1
대각보고 대각만큼 +1
나머지

인자에 N,1 어쩌고
이동 N되면 1로


'''
from collections import deque
import copy
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]
graph = []
move = deque()

N, M = map(int,input().split())
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
visited = [[0] *  N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))
for _ in range(M):
    d, s = map(int, input().split())
    # move.append((d, s))
    if d == 1:
        if cloud[0][0]+dr[0]*s < 0:
            cloud[0][0] = N-s
    elif d == 2:
    elif d == 3:
    elif d == 4:
    elif d == 5:
    elif d == 6:
    elif d == 7:
    elif d == 8:
        # 이걸 내가 모르고있는게 아니라 더 포커스가 잘못됨
        # 알고리즘 아이디어, 코드짜기, 이해
    # 대충 이해해서



'''
클라우드를 받아와
무브값 받아와서 이동시켜

'''


