"""
2
10 10 20 20
15 15 25 30
"""
MAX = 30001
import sys,math
input = sys.stdin.readline

N = int(input())
table = []

for _ in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    table.append([x1,y1, y2, True])
    table.append([x2,y1, y2, False])

table = sorted(table, key=lambda x:(x[0],x[1], x[2]))
height =int( math.ceil(math.log2(MAX)))
tree = [0] * (1<<(height+1))
seg = [0]* (1<<(height+1))

def update_range(idx, left,right, start, end, value):
    if left>end or right < start:
        return
    if left<=start and right>=end:
        tree[idx] += value
    else:
        mid = (start+end)//2
        update_range(idx*2, left,right, start, mid, value)
        update_range(idx*2+1, left, right, mid+1, end, value)
    
    
    if tree[idx] !=0:
        seg[idx] = (end-start+1)
    else:
        if start==end:
            seg[idx] =0
        else:
            seg[idx] = seg[idx*2]+seg[idx*2+1]




now = table[0]
total =0
update_range(1, now[1],now[2]-1, 0, MAX-1, 1)
for i in range(1, len(table)):
    new = table[i]
    dx = new[0] - now[0]
    total += dx * seg[1]

    if new[3]:
        update_range(1, new[1],new[2]-1, 0, MAX-1, 1)
    else:
        update_range(1, new[1], new[2]-1, 0,MAX-1, -1)
    
    now = new

print(total)