N = int(input())
'''
0에서 0은 0,1 선택가능
1에서 0은 0,1 선택가능 1은 1,2 선택가능
2에서 0은 0,1 , 1은 1,2 2는 2,3  
3에서 
i, j 
ij = max (i+1 j, i+1 j+1) 
'''
triangle = []
for i in range(N):
    triangle.append(list(map(int,input().split())))


for i in range(1,N):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == (len(triangle[i])-1):
            triangle[i][j] += triangle[i-1][len(triangle[i-1])-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[N-1]))