N = int(input())
inpt = []
for tc in range(N):
    inpt.append(str(input()))

stack = []
for i in inpt:
    if 'push' in i:
        i.strip()
        a = ''
        for j in i:
            if j == 'p' or j == 'u' or j == 's' or j == 'h':
                continue
            a += j
        stack.append(int(a))

    elif 'pop' in i:
        if not stack:
            print(-1)
        else:
            a = stack.pop()
            print(a)

    elif 'size' in i:
        print(len(stack))

    elif 'empty' in i:
        if not stack:
            print(1)
        else:
            print(0)

    elif 'top' in i:
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])


