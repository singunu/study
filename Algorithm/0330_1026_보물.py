N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
C = []

while A:
    C.append(min(A) * max(B))
    A.pop(0)
    for i in range(len(B)):
        if B[i] == max(B):
            B.pop(i)
            break

print(sum(C))