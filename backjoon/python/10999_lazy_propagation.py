"""
5 2 2
1
2
3
4
5
1 3 4 6
2 2 5
1 1 3 -2
2 2 5
"""
import sys
import math
input = sys.stdin.readline

n,m,k = map(int,input().split())

height = math.ceil(math.log2(n))

nn = 1<<(height+1)
sn = 1<<height
arr  = [0]*n
tree = [0]*nn
lazy = [0] * nn

def init(start, end, idx):
    global tree
    global lazy
    global arr
    if start==end:
        tree[idx] = arr[start]
    else:
        mid = (start+end)//2
        init(start, mid, idx*2)
        init(mid+1, end, idx*2+1)
        tree[idx] = tree[idx*2] + tree[idx*2+1]
        


def lazy_propagation(start, end, idx):
    if lazy[idx] !=0:
        tree[idx] += (end-start+1)*lazy[idx]
        if start != end:
            lazy[idx*2] += lazy[idx]
            lazy[idx*2+1] += lazy[idx]
        
        lazy[idx] = 0

def update_range(idx, left,right, start, end, value):
    lazy_propagation(start, end, idx)
    if left>end or right < start:
        return
    if left<=start and right>=end:
        tree[idx] += (end-start+1)*value
        if(start != end):
            lazy[idx*2] += value
            lazy[idx*2+1] += value
        return
    mid = (start+end)//2
    update_range(idx*2, left,right, start, mid, value)
    update_range(idx*2+1, left, right, mid+1, end, value)

    tree[idx] = tree[idx*2] + tree[idx*2+1]

def sum(idx, left, right, start, end):
    lazy_propagation(start, end,idx)
    if left > end or right < start:
        return 0
    if left<=start and right>=end:
        return tree[idx]

    mid = (start+end)//2

    return sum(idx*2, left, right, start, mid) + sum(idx*2+1, left, right, mid+1, end)




arr=[int(input()) for _ in range(n)]
init(0, n-1, 1)
val=[list(map(int,input().split())) for _ in range(m+k)]


for v in val:

    if v[0]==1:
        update_range(1, v[1]-1, v[2]-1, 0, n-1, v[3])
    else:
        print(sum(1, v[1]-1,v[2]-1, 0, n-1))

    
