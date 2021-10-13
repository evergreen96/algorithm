import sys
input = sys.stdin.readline


dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,m,x,y,k = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

commands = list(map(int,input().split()))
dices = [0]*7
for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]

    if not 0<=nx<n or not 0<=ny<m:
        continue
    
    x = nx
    y = ny
    if command==1:
        dices[1], dices[3], dices[6], dices[4] = dices[4], dices[1], dices[3], dices[6]
    elif command==2:
        dices[1], dices[3], dices[6], dices[4] = dices[3], dices[6], dices[4], dices[1]
    elif command==3:
        dices[1], dices[2], dices[5], dices[6] = dices[5], dices[1], dices[6], dices[2]
    else:
        dices[1], dices[2], dices[5], dices[6] = dices[2], dices[6], dices[1], dices[5]

    if table[nx][ny]==0:
        table[nx][ny] =  dices[6]
    else:
        dices[6] = table[nx][ny]
        table[nx][ny] = 0
    
    print(dices[1])
