N = int(input())
street = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * 4 for _ in range(N)]

for i in range(1,N):
    street[i][0] += min(street[i-1][1], street[i-1][2])
    street[i][1] += min(street[i-1][0], street[i-1][2])
    street[i][2] += min(street[i-1][1], street[i-1][0])

print(min(street[N-1][0],street[N-1][1],street[N-1][2]))

