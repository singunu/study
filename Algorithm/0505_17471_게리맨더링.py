







'''
for문으로 N개 돌리기
돌리는 i에서 i 1개당 1~ N개의 원소를 가지는 집합 만들기
만들고나서 visited_1 안된 것들로만 나머지 2번째 집합 만들기
집합이 이어지지 않는다면 (for문으로 인접리스트에 visited_2에만 있는 것으로 도달할 수 없다면)
그 경우의 수 폐기

'''
def solve(a,cnt):

    for i in range(1,cnt+1):
        


N = int(input())
population = list(map(int,input().split()))
adj = [[] for _ in range(N+1)]
for i in range(1,N+1):
    a = list(map(int,input().split()))
    del a[0]
    for j in a:
        adj[i].append(j)
result_lst = []
for i in range(1,N+1):
    result_lst.append(solve(i,1))