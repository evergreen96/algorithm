import sys
input = sys.stdin.readline


col, row = map(int, input().split())
x, y, d = map(int, input().split())

matrix = []
for _ in range(col):
    matrix.append(list(map(int, input().split())))
    
def show():
    for i in range(col):
        print(matrix[i])
    print()
visit = [[False]*row for _ in range(col)]


dc = [-1,0,1,0]
dr = [0,1,0,-1]

stack = [(x,y,d)]
total = 0
while stack:
    cc, cr, cd = stack.pop()
    if matrix[cc][cr] ==0 and visit[cc][cr]==False:
        total += 1
        visit[cc][cr] = True
    flag = False
    for i in range(4):
        nd = (cd+3)%4
        nc = cc + dc[nd]
        nr = cr + dr[nd]
        if 0<=nc<col and 0<=nr<row and  visit[nc][nr]==False and matrix[nc][nr]==0:
            flag = True
            stack.append((nc,nr, nd))
            break
        cd = nd
            
    
    if not flag:
        nd = (cd+2)%4
        nc = cc + dc[nd]
        nr = cr + dr[nd]
        if 0<=nc<col and 0<=nr<row:
            if matrix[nc][nr]==0:
                stack.append((nc,nr,cd))
            else:
                break

    

print(total)

"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

"""