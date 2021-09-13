n = int(input())
plans = input().split()

x,y = 1, 1

move = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

for plan in plans:
    if plan == "U":
        nx = x + move[0][0]
        ny = y + move[0][1]
    elif plan == "R":
        nx = x + move[1][0]
        ny = y + move[1][1]
    elif plan == "D":
        nx = x + move[2][0]
        ny = y + move[2][1]
    elif plan == "L":
        nx = x + move[3][0]
        ny = y + move[3][1]
    
    if nx < 1 or ny <1 or nx > n or ny >n :
        continue
    else:
        x,y = nx, ny
print(x, y)
