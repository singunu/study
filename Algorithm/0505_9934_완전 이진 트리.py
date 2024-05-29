



def inorder(s,e,level):
    if s == e:
        arr[level].append(tree[s])
        return

    mid = (s+e) // 2
    arr[level].append(tree[mid])

    inorder(s,mid-1, level+1)
    inorder(mid+1,e,level+1)

K = int(input())
tree = list(map(int,input().split()))
arr = [[] for _ in range(K)]
'''
2 -> 3 1+2
3 -> 7 1+2+4
4 -> 15 1+2+4+8
5 -> 31 1+2+4+8+16
'''
inorder(0,len(tree)-1,0)
for i in arr:
    print(*i)
