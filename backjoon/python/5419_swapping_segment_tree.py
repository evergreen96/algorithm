import sys
import math
input = sys.stdin.readline



def search(tree, cur, left, right, start, end):
    print(cur, start, end)
    if left > end or right < start:
        return 0
    if left<=start and right>=end:
        return tree[cur]
    mid = (start + end) // 2

    return search(tree, cur*2, left, right, start, mid) + search(tree, (cur*2)+1, left,right, mid+1, end)

def u2(tree, idx, h):
    idx = (1<<h) + idx
    tree[idx] += 1
    idx //= 2
    while(idx>0):
        tree[idx] = tree[idx*2] + tree[idx*2+1]
        idx //=2
    
def solution():
    n = int(input())
    table = []
    y_table = []
    for _ in range(n):
        x, y = map(int,input().split())
        table.append((x,y))
        y_table.append(y)
    table = sorted(table, key=lambda x:(x[0], -x[1]))

    y_table = list(set(y_table))
    y_table.sort()
    y_dict = { y_table[i] : i  for i in range(len(y_table))}
    h = math.ceil(math.log2(len(y_table)))
    print(h)
    t = 1<<h
    tree = [0]*(1<<(h+1))
    print(t)
    print(tree)
    result = 0
    for i in range(n):
        x, y = table[i]
        buf = search(tree, 1, y_dict[y], t-1, 0, t-1)
        result += buf
        u2(tree, y_dict[y], h)
    print(result)




N = int(input())
for _ in range(N):
    solution()

"""
10 10
1 0 1
2 0 0
3 1 1
1 0 1
1 0 1
2 0 0
3 1 1
1 0 1
"""
"""
1
4
-10 -10
-10 10
10 -10
10 10

2
4
-10 -10
-10 10
10 -10
10 10
3
1 3
2 2
3 1
"""


