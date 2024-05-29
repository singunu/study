arr = [list(map(int, input().split())) for _ in range(19)]
winner = 0
dr = [0,1,1,-1]
dc = [1,0,1,1]
black = 0
white = 0
check = 0
idx = []
visited = [[-1] * 19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1 and not check:

            for d in range(4):
                black_cnt = 1
                for k in range(1,6):
                    di = i + dr[d] * k
                    dj = j + dc[d] * k
                    if 0 <= di < 19 and 0 <= dj < 19:

                        if k < 5:
                            if arr[di][dj] != 1:
                                black_cnt = 1
                                break
                        if arr[di][dj] == 1:
                            black_cnt += 1

                        if k == 5 and black_cnt > 5:


                if black_cnt == 5:
                    check = 1
                    black = 1
                    idx.append(i+1)
                    idx.append(j+1)
                    break
                else:
                    black_cnt = 1

        elif arr[i][j] == 2 and not check:

            for d in range(4):
                white_cnt = 1
                for k in range(1,6):
                    di = i + dr[d] * k
                    dj = j + dc[d] * k
                    if 0 <= di < 19 and 0 <= dj < 19:

                        if k < 5:
                            if arr[di][dj] != 2:
                                white_cnt = 1
                                break
                        if arr[di][dj] == 2:
                            white_cnt += 1

                if white_cnt == 5:
                    check = 2
                    white = 2
                    idx.append(i+1)
                    idx.append(j+1)
                    break
                else:
                    white_cnt = 1
        if check:
            break
    if check:
        break

if black:
    print(black)
    for i in idx:
        print(i,end=' ')
elif white:
    print(white)
    for i in idx:
        print(i, end=' ')
elif not black and not white:
    print(0)


