N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)

def solve():
    global K
    cnt = 0
    for i in range(N):
        if K <= 0:
            break
        if K >= coin[i]:
            cnt += (K // coin[i])
            K %= coin[i]
    return cnt

result = solve()
print(result)