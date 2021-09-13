
"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
"""

n = int(input())

table = []
loclist = []

for i in range(n):
    tmp = list(map(str, input().split()))
    table.append(tmp)
    for j in range(n):
        if tmp[j]=="T":
            loclist.append((i, j))

if len(loclist)==0:
    print("YES")
    exit()

def showing():
    for row in table:
        print(row)
    print()

def check():
    for x, y in loclist:
        for i in range(y+1, n):
            if table[x][i] =="S":
                return False
            if table[x][i] =="O":
                break
            if table[x][i] == "X":
                continue
        
        for i in range(y-1, -1, -1):
            if table[x][i] == "S":
                return False
            if table[x][i] == "O":
                break
            if table[x][i] == "X":
                continue
        
        for i in range(x+1, n):
            if table[i][y] =="S":
                return False
            if table[i][y]=="O":
                break
            if table[i][y] == "X":
                continue
        for i in range(x-1, -1, -1):
            if table[i][y] =="S":
                return False
            if table[i][y]=="O":
                break
            if table[i][y] == "X":
                continue

    
    return True

answer = False

def dfs(count):
    global answer
    if count == 3:
        result = check()
        if result:
            print("YES")
            exit()
    else:
        for i in range(n):
            for j in range(n):
                if table[i][j] == "X":
                    table[i][j]="O"
                    dfs(count+1)
                    table[i][j]="X"


dfs(0)

print("NO")

