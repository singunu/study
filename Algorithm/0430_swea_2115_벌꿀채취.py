

import itertools

def solve(a,b):
    max_v = 0
    lst = []
    for i in range(b,b+M):
        lst.append(arr[a][i])
    com_lst = []
    for i in range(M):
        for j in itertools.combinations(lst,i+1):
            com_lst.append(j)
    for i in com_lst:
        if sum(i) <= C:
            square_com = []
            for j in i:
                square_com.append(j ** 2)
            if max_v < sum(square_com):
                max_v = sum(square_com)
    return max_v

'''
함수 안에서 해야할 일
max값 = 0 초기화
인덱스값 받아와서
for문으로 j부터 j+M-1개까지 돌리기
if 조합의 sum이 C보다 작을때만
조합 안에서 for문으로 제곱값 임시 리스트에 넣어주기
다 넣고나서 max_v랑 비교해서 갈아치우기
sum(제곱된 값) 리턴

'''

#해야할게 뭐냐
# 포문 돌리면서 가로로 0부터 j+M <= N 까지 돌리기
# 일꾼1이 M개 체크하면 visited
# 일꾼2가 체크 안된 곳 중에 j+M <= N를 벗어나지 않는 한에서 탐색
# 포문 2개 돌려서 일꾼1 돌리고 그 밑에 포문 2개 돌려서 일꾼2 돌리기
# 일꾼1 돌릴때 리턴값 임시저장, 일꾼2 돌릴때 리턴값 리스트에 일꾼1과함꼐 더해서 저장
#

T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result_lst = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > C:
                continue
            if j+M <= N:
                result_1 = solve(i,j)

                for v in range(j,j+M):
                    visited[i][v] = 1

                for x in range(N):
                    for y in range(N):
                        if i == x:
                            continue
                        if not visited[x][y] and y+M <= N:
                            if arr[x][y] > C:
                                continue
                            result_2 = solve(x,y)
                            result_lst.append(result_1 + result_2)
            visited = [[0] * N for _ in range(N)]   # 일꾼2가 다돌면 초기화
    print(f'#{tc} {max(result_lst)}')