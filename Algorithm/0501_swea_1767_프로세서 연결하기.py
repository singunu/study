from collections import deque

def up(idx,lst,core,wire):
    global max_core
    global core_cnt
    if idx >= len(idx_lst):
        core_and_wire.append([core,wire])
        return
    x = idx_lst[idx][0]
    y = idx_lst[idx][1]
    wire_check = 0
    check_idx = deque()
    for i in range(x-1,-1,-1):
        if lst[i][y]:
            core_and_wire.append([core, wire])
            return
        check_idx.append(i)
        wire_check += 1
    for i in check_idx:
        lst[i][y] += 1
    wire += wire_check
    core += 1

    if core > core_cnt:
        core_cnt = core

    copy_lst = [c[:] for c in lst]
    up(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 1, copy_lst, core, wire)

    if core_cnt == max_core:
        return

    copy_lst = [c[:] for c in lst]
    up(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 2, copy_lst, core, wire)

def down(idx,lst,core,wire):
    global max_core
    global core_cnt
    if idx >= len(idx_lst):
        core_and_wire.append([core,wire])
        return
    x = idx_lst[idx][0]
    y = idx_lst[idx][1]
    wire_check = 0
    check_idx = deque()
    for i in range(x+1,N):
        if lst[i][y]:
            core_and_wire.append([core, wire])
            return
        check_idx.append(i)
        wire_check += 1
    for i in check_idx:
        lst[i][y] += 1
    wire += wire_check
    core += 1

    if core > core_cnt:
        core_cnt = core

    copy_lst = [c[:] for c in lst]
    up(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 1, copy_lst, core, wire)

    if core_cnt == max_core:
        return

    copy_lst = [c[:] for c in lst]
    up(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 2, copy_lst, core, wire)

def right(idx,lst,core,wire):
    global max_core
    global core_cnt
    if idx >= len(idx_lst):
        core_and_wire.append([core,wire])
        return
    x = idx_lst[idx][0]
    y = idx_lst[idx][1]
    wire_check = 0
    check_idx = deque()
    for i in range(y+1,N):
        if lst[x][i]:
            core_and_wire.append([core, wire])
            return
        check_idx.append(i)
        wire_check += 1
    for i in check_idx:
        lst[x][i] += 1
    wire += wire_check
    core += 1

    if core > core_cnt:
        core_cnt = core

    copy_lst = [c[:] for c in lst]
    up(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 1, copy_lst, core, wire)

    if core_cnt == max_core:
        return

    copy_lst = [c[:] for c in lst]
    up(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 2, copy_lst, core, wire)

def left(idx,lst,core,wire):
    global max_core
    global core_cnt
    if idx >= len(idx_lst):
        core_and_wire.append([core,wire])
        return
    x = idx_lst[idx][0]
    y = idx_lst[idx][1]
    wire_check = 0
    check_idx = deque()
    for i in range(y-1,-1,-1):
        if lst[x][i]:
            core_and_wire.append([core, wire])
            return
        check_idx.append(i)
        wire_check += 1
    for i in check_idx:
        lst[x][i] += 1
    wire += wire_check
    core += 1

    if core > core_cnt:
        core_cnt = core

    copy_lst = [c[:] for c in lst]
    up(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 1, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 1, copy_lst, core, wire)

    if core_cnt == max_core:
        return

    copy_lst = [c[:] for c in lst]
    up(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    down(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    right(idx + 2, copy_lst, core, wire)
    copy_lst = [c[:] for c in lst]
    left(idx + 2, copy_lst, core, wire)

def dfs():
    global max_core
    global core_cnt
    lst = [c[:] for c in visited]
    up(0, lst, 0, 0)
    lst = [c[:] for c in visited]
    down(0, lst, 0, 0)
    lst = [c[:] for c in visited]
    right(0, lst, 0, 0)
    lst = [c[:] for c in visited]
    left(0, lst, 0, 0)
    if core_cnt == max_core:
        return
    lst = [c[:] for c in visited]
    up(1, lst, 0, 0)
    lst = [c[:] for c in visited]
    down(1, lst, 0, 0)
    lst = [c[:] for c in visited]
    right(1, lst, 0, 0)
    lst = [c[:] for c in visited]
    left(1, lst, 0, 0)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    core_and_wire = []
    max_core = 0
    core_cnt = 0
    idx_lst = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] and (i == 0 or i == N - 1 or j == 0 or j == N - 1):
                arr[i][j] = 2
                visited[i][j] = 1
            elif arr[i][j] == 1:
                idx_lst.append((i,j))
                visited[i][j] = 1
                max_core += 1

    dfs()
    core_and_wire.sort(key=lambda x : (-x[0], x[1]))
    result = core_and_wire[0][1]
    print(f'#{tc} {result}')