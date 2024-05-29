N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
result = [0] * len(A)
cnt = 0
w = 0
for i in range(len(A)):
    A[i] -= B
    cnt += 1
for i in range(len(A)):
    if A[i] > 0:
        if A[i] % C:
           w = A[i] // C + 1
        else:
           w = A[i] // C
        result[i] += w

print(sum(result)+cnt)


