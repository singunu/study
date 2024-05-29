from itertools import combinations
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i,j])
        if graph[i][j] == 2:
            chicken.append([i,j])

print(house)
print(chicken)
result_distance = 99999999
for com in list(combinations(chicken, M)):  # 집과 치킨집 전체 조합
    distance_sum = 0            # 최소 거리 더한 값
    for x,y in house:           # 집 좌표 [x][y]
        distance = 99999999
        for a,b in com:         # 치킨집 좌표 [a][b]
            distance = min(distance,abs(x-a)+abs(y-b))
        distance_sum += distance
    result_distance = min(distance_sum,result_distance)
print(result_distance)





from itertools import combinations
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i,j])
        if graph[i][j] == 2:
            chicken.append([i,j])

result_distance = N ** 2 * 2
for com in list(combinations(chicken, M)):
    distance_sum = 0
    for x,y in house:
        distance = N ** 2 * 2
        for a,b in com:
            distance = min(distance,abs(x-a)+abs(y-b))
        distance_sum += distance
    result_distance = min(distance_sum,result_distance)
print(result_distance)