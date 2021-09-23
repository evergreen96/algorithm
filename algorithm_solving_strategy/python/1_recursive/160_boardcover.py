import sys
input = sys.stdin.readline

n = int(input())

rotationlist = [
    [[0,0], [1,0], [0,1]],
    [[0,0], [0,1], [1, 1]],
    [[0,0], [1,0], [1, 1]],
    [[0,0], [1,0], [1, -1]],
       
]


def dfs( table, col, row):
    flag = True

    x,y = (0,0)
    for i in range(col):
        for j in range(row):
            if table[i][j]==".":
                flag = False
                x, y = i, j
                break
        if flag==False:
            break
    if flag==True:
        return 1

    total  = 0
    for i in range(4):
        a1, b1 = x+rotationlist[i][0][0], y + rotationlist[i][0][1]
        a2, b2 = x+rotationlist[i][1][0], y + rotationlist[i][1][1]
        a3, b3 = x+rotationlist[i][2][0], y + rotationlist[i][2][1]

        if (0<= a1 < col) and (0<= a2 < col) and (0<= a3 < col) and (0<= b1 < row) and (0<= b2 < row) and (0<= b3 < row ):
            if table[a1][b1]=="." and table[a2][b2]=="."and table[a3][b3]==".":
                table[a1][b1] = "#"; table[a2][b2]='#';  table[a3][b3] = "#"
                total += dfs(table, col, row)
                table[a1][b1] = "."; table[a2][b2]='.';  table[a3][b3] = "."

    return  total
    

def solution():
    col, row = map(int, input().split())
    table = []
    for _ in range(col):
        table.append(list(input().rstrip()))

    whiteCnt = 0
    for i in range(col):
        for j in range(row):
                whiteCnt += 1
    if whiteCnt==0:
        print(0)
        return

    total = dfs(table, col, row)
    print(total)

for _ in range(n):
    solution()


"""
1
3 7 
#.....# 
#.....# 
##..### 
1
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 

3 
3 7 
#.....# 
#.....# 
##...## 
3 7 
#.....# 
#.....# 
##..### 
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 
"""