from collections import deque

def solve():
    queue = deque()
    for i in range(N):
        queue.append(trucks[i])

    bridge = deque()
    cnt = 1
    arr = [0] * W
    while queue or bridge:

        if queue:
            if sum(bridge) + queue[0] <= L and len(bridge) <= W:
                bridge.append(queue.popleft())
                arr[0] = 1

        for i in range(W-1,-1,-1):
            if arr[i] == 1:
                arr[i] = 0
                if i < W-1:
                    arr[i+1] = 1
                else:
                    arr[i] = 0
                    bridge.popleft()
        cnt += 1

    return cnt

'''
브릿지 렌만큼 w, w-1, w-2식으로 초에 계산
더하는 값이 L보다 작을때만 더하기
'''
N, W, L = map(int,input().split())
trucks = (list(map(int,input().split())))
print(solve())