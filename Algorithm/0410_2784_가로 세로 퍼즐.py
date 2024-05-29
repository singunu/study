import copy
puzzle = [str(input()) for _ in range(6)]
puzzle.sort()
board = [[''] * 3 for _ in range(3)]
result = []
for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == j or i == k or j == k:
                continue
            tmp = [puzzle[i], puzzle[j], puzzle[k]]
            tmp2 = tmp.copy()
            for h in range(3):
                tmp2.append(tmp[0][h] + tmp[1][h] + tmp[2][h])
            tmp2.sort()
            if puzzle == tmp2:
                result.append(tmp[0] + tmp[1] + tmp[2])
result.sort()



