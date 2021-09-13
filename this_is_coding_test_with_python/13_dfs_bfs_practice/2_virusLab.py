import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split(' '))))

buff = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


maxRoom = 0


def spread(x,y):
    global buff
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and buff[nx][ny]==0:
            buff[nx][ny]=2
            spread(nx, ny)


def check():
    global buff
    rooms = 0
    for i in range(n):
        for j in range(m):
            if buff[i][j]==0:
                rooms += 1
    return rooms


def dfs(start, count):
    global maxRoom, arr, buff
    if count != 3:
        for i in range(start, n*m):
            x = i//m
            y = i% m
            if arr[x][y]==0:
                arr[x][y]=1
                dfs(i+1, count+1)
                arr[x][y]=0
        """
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    arr[i][j]=1
                    count += 1
                    dfs(count)
                    arr[i][j] = 0
                    count -= 1
        """
    else:
        buff = copy.deepcopy(arr)

        for i in range(n):
            for j in range(m):
                if buff[i][j]==2:
                    spread(i,j)
        maxRoom = max(maxRoom, check())
        return


dfs(0,0)
print(maxRoom)