import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
table = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int, input().split())
    table[a][b] = 1

def show():
    for i in range(1, len(table)):
        print(table[i][1:])


dy = [-1,0,1,0]
dx = [0,1,0,-1]

cmds = []
l = int(input())
for _ in range(l):
    a,b = input().split()
    cmds.append((int(a),b))

def turn(dir, cmd):
    if cmd=="L":
        return 3 if dir-1<0 else dir-1
    else:
        return (dir+1) % 4

y, x, d= 1,1,1
time = 0 
table[y][x] = 2
q = [(y,x)]

while True:
    ny = y + dy[d]
    nx = x + dx[d]
    time += 1
    if 1<=ny<=n and 1<=nx<=n and table[ny][nx]!=2:
        if table[ny][nx] == 0:
            yy, xx = q.pop(0)
            table[yy][xx] = 0
    else:
        break
    table[ny][nx] = 2
    q.append((ny,nx))
    y = ny
    x = nx
    if len(cmds)>0 and time == cmds[0][0]:
        cmd = cmds[0]
        cmds = cmds[1:]
        d  = turn(d, cmd[1])
    
print(time)


"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""