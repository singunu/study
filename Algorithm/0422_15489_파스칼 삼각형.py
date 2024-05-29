R, C, W = map(int,input().split())
'''
R 번째 줄
C 번째 수 가 꼭짓점
W 길이의 정삼각형 
크기
R+W-1만큼
'''
dp = [[] for _ in range(R+W)]
dp[0].append(1)
for i in range(1,R+W):
    for j in range(i+1):
        if not j:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j]+dp[i-1][j-1])
a = 0
result = 0
for i in range(R-1,W+R-1):
    for j in range(C-1, a+C):
        result += dp[i][j]
    a += 1
print(result)
