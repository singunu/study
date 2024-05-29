N = int(input())
arr = []
for tc in range(N):
    a = int(input())
    arr.append(a)

result = []
for i in range(len(arr)):
    if arr[i] == 0:
        result.pop()
    else:
        result.append(arr[i])

print(sum(result))