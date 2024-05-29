N = int(input())
n = N
a = 0
for i in range(1,N+1):
    if n - i <= 0:
        a = i
        break
    n -= i

if a % 2:
    x = a - n + 1
    y = n
else:
    x = n
    y = a - n + 1

print(f'{x}/{y}')

