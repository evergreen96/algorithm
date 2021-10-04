import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())

table = []
table.append([0]*(m+1))

for _ in range(n):
     tmp = [0]
     tmp += list(map(int,input().rstrip()))
     table.append(tmp)

visit = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]
q = deque()
visit[1][1][1] = 1

q.append((1,1,1))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    col, row, wall = q.popleft()

    if col==n and row==m:
        print(visit[col][row][wall])
        exit()
    
    for i in range(4):
        nc = col + dy[i]
        nr = row + dx[i]
        if 1<=nc<=n and 1<=nr<=m:
            if table[nc][nr] == 0 and visit[nc][nr][wall]==0:
                visit[nc][nr][wall] = visit[col][row][wall] + 1
                q.append([nc, nr, wall])
            elif table[nc][nr] == 1 and wall==1:
                visit[nc][nr][0] = visit[col][row][1] + 1
                q.append([nc,nr,0])

print(-1)
"""
6 4
0100
1110
1000
0000
0111
0000
"""

"""

import sys
from collections import deque
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())


table = []
table.append([0]*(m+1))
for _ in range(n):
     tmp = [0]
     tmp += list(map(int,input().rstrip()))
     table.append(tmp)

# m, n

visit = [[0]*(m+1) for _ in range(n+1)]

total = 0
q = []
visit[1][1] = 1
heapq.heappush(q,(1,1,1,1))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
total = int(1e9)
flag = False
while q:
    cnt, col, row, limit = heapq.heappop(q)
    if visit[col][row] < cnt:
        continue
    
    if col==n and row==m:
        flag = True
        if total > cnt:
            total = cnt

    for i in range(4):
        nc = col + dy[i]
        nr = row + dx[i]

        if 1<=nc<=n and 1<=nr<=m:
            if visit[nc][nr]==0: 
                if table[nc][nr] == 1:
                    if limit==1:
                        visit[nc][nr] = cnt+1
                        table[nr][nr] = 0
                        heapq.heappush(q,(cnt+1, nc,nr, 0))
                elif table[nc][nr]==0:
                    visit[nc][nr] = cnt+1
                    heapq.heappush(q,(cnt+1, nc,nr, limit))


if flag:
    print(total)
else:

    print(-1)


"""