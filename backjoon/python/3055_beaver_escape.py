import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
input = sys.stdin.readline
n,m = map(int, input().split())

table = []

for _ in range(n):
    table.append(list(map(str,input().rstrip())))

dest = (0,0)
start = (0.0)
for i in range(n):
    for j in range(m):
        if table[i][j]=="D":
            dest =  (i, j)
        if table[i][j]=="S":
            start = (i, j)

def spread():
    water_loc = []
    for i in range(n):
        for j in range(m):
            if table[i][j]=="*":
                water_loc.append((i, j))

    for i, j in water_loc:
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]

            if 0<=ni<n and 0<=nj<m:
                if table[ni][nj]=="." or table[ni][nj]=="S":
                    table[ni][nj]="*"

flag = False

q = deque()
q.append((start[0], start[1], 0))

def show():
    for i in range(n):
        print(table[i])
    print()

ret = -1

jump = -1
while q:
    col, row, time = q.popleft()
    if (col,row) ==dest:
        ret = time
        break
    if jump != time:
        spread()
        jump = time

    for i in range(4):
        nc = col + dy[i]
        nr = row + dx[i]
        if 0<=nc<n and 0<=nr<m:
            if table[nc][nr]=="." or table[nc][nr]=="D":
                table[nc][nr]="S"
                q.append((nc, nr, time+1))

if ret==-1:
    print("KAKTUS")
else:
    print(ret)


#  물이 차있는 지역은 '*', 돌은 'X'
# KAKTUS
"""
3 3
D.*
...
.S.
"""