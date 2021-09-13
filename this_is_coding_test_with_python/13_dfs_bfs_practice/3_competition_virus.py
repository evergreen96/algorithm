import sys, copy
import heapq
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

table = []
idxlist = []
q = deque()
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

for i in range(n):
    for j in range(n):
        if table[i][j] != 0:
            idxlist.append((table[i][j], i, j, 0))

idxlist.sort()

q = deque(idxlist)

s, x, y = map(int, input().split())
dx = [-1, 0 ,1 ,0]
dy = [0, 1, 0 , -1]

while q:
    v, a, b, tt = q.popleft()
    if tt==s:
        break
    for t in range(4):
        na = a + dx[t]
        nb = b + dy[t]
        if 0<=na < n and 0<=nb <n and table[na][nb]==0:
            table[na][nb]=v
            q.append((v, na, nb, tt+1))


print(table[x-1][y-1])