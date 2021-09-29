
def update(tree, x, y, value):
    while x<len(tree):
        ty = y
        while(ty<len(tree[0])):
            tree[x][ty] += value
            ty += (ty&-ty)
        
        x += (x & -x)

def sum(tree, x, y):
    ret = 0
    while(x>0):
        ty = y
        while ty > 0:
            ret += tree[x][ty]
            ty -= (ty&-ty)
        
        x -= (x & -x)
    return ret

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = [[0]*(n+1)]
tree = [[0]*(n+1) for _ in range(n+1)]




for i in range(1, n+1):
    tmp = [0]
    tmp += list(map(int, input().split()))
    arr.append(tmp)

for i in range(1, n+1):
    for j in range(1, n+1):
        update(tree, i, j, arr[i][j])



for _ in range(k):
    v = list(map(int,input().split()))
    if v[0]==0:
        diff =  v[3] - arr[v[1]][v[2]]
        update(tree, v[1],v[2], diff)
        arr[v[1]][v[2]] = v[3]
    else:
        a = sum(tree,v[3],v[4])
        b = sum(tree,v[3],v[2]-1)
        c = sum(tree,v[1]-1, v[4])
        d = sum(tree, v[1]-1, v[2]-1)
        print(a-b-c+d)


"""
4 5
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 2 2 3 4
0 2 3 7
1 2 2 3 4
0 3 4 5
1 3 4 3 4
"""