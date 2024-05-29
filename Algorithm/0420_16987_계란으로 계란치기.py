N = int(input())
egg_lst = [list(map(int, input().split())) for _ in range(N)]
def dfs(c, cnt):
    global result
    if result >= cnt+(N-c) * 2:
        return
    if c == N:
        result = max(result, cnt)
        return

    if egg_lst[c][0] <= 0:
        dfs(c+1, cnt)

    else:
        is_crushed = False
        for i in range(N):
            if i != c and egg_lst[i][0] > 0:
                egg_lst[c][0] -= egg_lst[i][1]
                egg_lst[i][0] -= egg_lst[c][1]
                is_crushed = True
                dfs(c+1, cnt + int(egg_lst[c][0] <= 0) + int(egg_lst[i][0] <= 0))
                egg_lst[c][0] += egg_lst[i][1]
                egg_lst[i][0] += egg_lst[c][1]

        if not is_crushed:
            dfs(c+1, cnt)

result = 0
dfs(0,0)
print(result)

# N = int(input())
# egg_lst = []
# for n in range(N):
#     egg_lst.append(list(map(int,input().split())))
#     egg_lst[n].append(n)

# def crush_egg(c):
#     current = egg_lst.pop(c)
#     egg_lst.sort(key=lambda x: (x[1], x[0]))
#     for i in range(len(egg_lst)):
#         if egg_lst[i][0] <= 0:
#             continue
#
#         current[0] -= egg_lst[i][1]
#         egg_lst[i][0] -= current[1]
#
#         if current[0] <= 0 and egg_lst[i][0] > 0:   # 커렌트 깨지고 뒤에꺼 안깨지면 함수 재시작
#             egg_lst.append(current)
#             egg_lst.sort(key=lambda x: (x[2]))
#             return
#
#         if current[0] > 0 and egg_lst[i][0] <= 0:   # 커렌트 안깨지고 뒤에꺼 깨지면 for문 다음 i로 넘어가기
#             continue
#
#         if current[0] > 0 and egg_lst[i][0] > 0:    # 커렌트 안깨지고 뒤에꺼 안깨지면
#             egg_lst.append(current)
#             egg_lst.sort(key=lambda x: (x[2]))
#             return
#
#         if current[0] <= 0 and egg_lst[i][0] <= 0:  # 커렌트 꺠지고 뒤에꺼도 깨지면
#             egg_lst.append(current)
#             egg_lst.sort(key=lambda x: (x[2]))
#             return
#     else:
#         egg_lst.append(current)
#         egg_lst.sort(key=lambda x: (x[2]))
#         return
#
# for i in range(N):
#     if egg_lst[i][0] > 0:
#         crush_egg(i)
#
# cnt = 0
# for egg in egg_lst:
#     if egg[0] <= 0:
#         cnt += 1
# print(cnt)