import sys
from collections import deque
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())

table = []
table.append([0]*(n+1))
for _ in range(m):
     tmp = [0]
     tmp += list(map(int,input().rstrip()))
     table.append(tmp)

# m, n

visit = [[0]*(n+1) for _ in range(m+1)]

total = 0
q = []
visit[1][1] = 1
q.append((1,1,1))
heapq.heappush(q,(1,1,1))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    cnt, col, row = heapq.heappop(q)
    if visit[col][row] < cnt:
        continue
    
    if col==m and row==n:
        print(cnt-1)
        break

    for i in range(4):
        nc = col + dy[i]
        nr = row + dx[i]

        if 1<=nc<=m and 1<=nr<=n:
            if visit[nc][nr]==0: 
                if table[nc][nr] == 1:
                    visit[nc][nr] = cnt+1
                    heapq.heappush(q,(cnt+1, nc,nr))
                else:
                    visit[nc][nr] = cnt
                    heapq.heappush(q,(cnt, nc,nr))



"""
3 3
011
111
110
"""
