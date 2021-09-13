from collections import deque
import sys
input = sys.stdin.readline
n,l,r = map(int, input().split())

table  = []
visited = [[0]*n for _ in range(n)]
for _ in range(n):
    table.append(list(map(int, input().split())))

total_cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if l <= abs(table[nx][ny]-table[x][y]) <= r:
                return True


flag = False

def bfs(a,b):
    global flag
    q = deque()
    q.append((a,b))
    result = []
    visited[a][b]=1
    sub_total = table[a][b]
    while q:
        x, y = q.popleft()
        result.append((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                gap = abs(table[x][y]-table[nx][ny])
                if l<=gap <=r:
                    flag = True
                    visited[nx][ny] = 1
                    sub_total += table[nx][ny]
                    q.append((nx, ny))
    sub_total //= len(result)
    for (x, y) in result:
        table[x][y] = sub_total



while True:
    for i in range(n):
        for j in range(n):
            if check(i,j) and visited[i][j]==0:
                bfs(i, j)
    
    if flag==False:
        print(total_cnt)
        exit()
    else:
        total_cnt += 1
        visited = [[0]*n for _ in range(n)]
        flag = False


"""
2 20 50
50 30
20 40

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

3 5 10
10 15 20
20 30 25
40 22 10
"""
