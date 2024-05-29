N = int(input())
arr = list(map(int,input().split()))
arr.sort()
sum_v = 0
sum_lst = []
for i in range(N):
    sum_v += arr[i]
    sum_lst.append(sum_v)
print(sum(sum_lst))
