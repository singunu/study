from itertools import permutations, combinations

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
min_result = 9999999
idx = []
for i in range(N):
    idx.append(i)
com = list(combinations(idx,N//2))
idx_unit = []
for i in range(len(com)):
    idx_unit.append(list(permutations(com[i],2)))
idx_1 = idx_unit[0:len(idx_unit)//2]
idx_2 = idx_unit[len(idx_unit)-1:len(idx_unit)//2-1:-1]
for i in range(len(idx_1)):
    r = 0
    e = 0
    for j in range(len(idx_1[0])):
        r += arr[idx_1[i][j][0]][idx_1[i][j][1]]
        e += arr[idx_2[i][j][0]][idx_2[i][j][1]]

    if min_result > abs(r-e):
        min_result = abs(r-e)
print(min_result)

