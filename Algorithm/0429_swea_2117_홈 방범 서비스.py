def solve(x, y, c):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if abs(x-i) + abs(y-j) < c:
                if arr[i][j]:
                    cnt += 1
    return cnt

'''
함수안에서 할일
인덱스 받아와서 포문 돌리면서 조건으로 1(집있는곳) 찾고 갯수 반환

'''

# 커지는 대각선의 규칙 수식
# abs(i-x) + abs(j-y) 가 k보다 작아야함
# 비용은 k ** 2 + (k-1) ** 2
# 다 돌면서 비용 걷고 k 계산 한다음 max값 도출
# k개 돌리고
# 한자리씩 돌리고
# visited로 집갯수 담고
# k 담고
# k는 몇개부터 몇개까지할까
# n이 5일떄

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result_lst = []
    for i in range(N):
        for j in range(N):
            for k in range(1,N+2):
                # if k == N+1:
                #     if i < N / 2 - 2 and i > N / 2 + 2 and j < N / 2 - 2 and j > N / 2 + 2:
                #         continue
                # else:
                result = solve(i, j, k)
                result_lst.append([M * result - (k * k + (k-1) * (k-1)), result])
    house_cnt = 0
    for i in range(len(result_lst)):
        if result_lst[i][0] >= 0:
            if result_lst[i][1] > house_cnt:
                house_cnt = result_lst[i][1]
    print(f'#{tc} {house_cnt}')