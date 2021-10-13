from collections import deque
table = []

for _ in range(3):
    table.append(list(map(int,input().split())))

col = 0
row = 0

dc = [1,-1 ,0, 0]
dr = [0, 0, 1, -1]

for i in range(3):
    for j in range(3):
        if table[i][j]==0:
            col = i
            row = j
            break

def check():
    for i in range(3):
        for j in range(3):
            if i==2 and j==2 and table[i][j]==0:
                return True
            if (i*3) + (j+1) != table[i][j]:
                return False
    return True

def is_wring(c, r):
    if (c*3)+ (r+1) != table[c][r]:
        return True
    return False

def show():
    for i in range(3):
        print(table[i])
    print()

q = deque()
q.append((col, row, 0))
while  q:
    nc, nr, cnt = q.popleft()
    if check():
        print(cnt)
        exit()
    
    for i in range(4):
        nnc = nc + dc[i]
        nnr = nr + dr[i]
        if 0<=nnc < 3 and 0<=nnr<3:
            if is_wring(nnc, nnr):
                table[nc][nr], table[nnc][nnr] = table[nnc][nnr], table[nc][nr]
                #nc, nr = nnc, nnr
                q.append((nnc,nnr, cnt+1))

print(-1)
"""
1 0 3
4 2 5
7 8 6

3 6 0
8 1 2
7 4 5
"""
