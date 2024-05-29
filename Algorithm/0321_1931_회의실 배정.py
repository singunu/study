'''
각 집합을 안 겹치게 조합하는 경우의 수 중
가장 많이 집합을 포함할 수 있는 max_v를 찾아라
0자리보다
'''
N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))
s = 0
result = []
for i in range(N):
    if s <= meeting[i][0]:
        s = meeting[i][1]
        result.append(meeting[i])
print(len(result))