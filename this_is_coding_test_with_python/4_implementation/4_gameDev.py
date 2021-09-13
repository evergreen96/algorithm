n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, di = map(int, input().split())

d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


dx = [-1, 0 , 1 ,0]
dy = [0, 1, 0 ,-1]

def rotation():
    global di
    di -= 1
    if di == -1:
        di =3 

cnt = 1
turns = 0
while True:
    rotation()
    nx = x + dx[di]
    ny = y + dy[di]

    if arr[nx][ny] == 0 and d[nx][ny]==0:
        d[nx][ny] = 1
        cnt += 1
        turns = 0
        x = nx; y = ny
    else:
        turns += 1
    
    if turns == 4:   
        nx = x - dx[di]
        ny = y - dy[di]

        if arr[nx][ny]==0:
            x = nx
            y = ny
        else:
            break
        turns = 0 

print(cnt)        