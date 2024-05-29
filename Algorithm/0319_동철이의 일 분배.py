def solve(row, mul_v):                              # row는 행, i는 열
    global max_v
    if row == N:
        if mul_v >= max_v:
            max_v = mul_v
        return

    for i in range(N):                              # 0, 1, 2 돌면서
        if mul_v * arr[row][i] <= max_v:
            continue
        if col[i] == 0:                           # 안 쓴 열이면
            col[i] = 1                              # 썼다 표시하고
            solve(row + 1, mul_v * arr[row][i])     # sum_v에 그 행을 더하고 재귀
            col[i] = 0                              # 함수 호출 후엔 썼다는 표시 지우기
    return max_v * 100

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x: float(x) * 0.01, input().split())) for _ in range(N)]
    col = [0] * N
    max_v = float(-1)

    result = solve(0,1)
    print(f'#{tc} {result:.6f}')

