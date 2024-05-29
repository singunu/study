
# def solve(num):
#     global max_v
#     if num == 0:
#         return print(max_v)
#     if arr[0] * num > max_v:
#         max_v = arr[0] * num
#     arr.pop(0)
#     solve(num-1)
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
# max_v = 0
# solve(N)



N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
m = []

for i in range(N):
    m.append(arr[i]*N)
    N -= 1

print(max(m))