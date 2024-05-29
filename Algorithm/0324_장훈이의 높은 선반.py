def dfs(cnt, sum_v):
    global lst
    if sum_v >= B:
        lst.append(sum_v)
        return
    if cnt == N:
        return

    dfs(cnt + 1, sum_v)
    dfs(cnt + 1, sum_v + S[cnt])


T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    S = list(map(int, input().split()))
    lst = []
    dfs(0, 0)
    print(f'#{tc} {min(lst) - B}')

# B 이상인 경우 return
# B - result 출력
# 리스트에 경우의 수 다 집어넣고
# min 리턴