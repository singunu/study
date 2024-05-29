input_list = []
N = int(input())
for tc in range(N):
    input_list.append(str(input()))

def solve(x):
    global cnt
    visited = []
    checker = 'A'
    for i in x:
        if i != checker:
            if i not in visited:
                checker = i
                visited.append(i)
            elif i in visited:
                return
    cnt += 1
'''
체커랑 같을때 방문한적 없을때는 존재할 수 없음
체커랑 같을때 방문한적 있을때 이어가기
체커랑 다를때 방문한적 없을때 체커 바꿔주고 방문표시
체커랑 다를때 방문한적 있을때 리턴

'''

cnt = 0
for i in input_list:
    solve(i)
print(cnt)