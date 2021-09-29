



n,m = map(int, input().split())

command = int(input())

default_table = []
table = []
for _ in range(command):
    x1,y1, x2,y2, d = map(int,input().split())
    table[x1][y1] += d
    table[x2+1][y1+1] += d
    table[x1][y2+1] = -d
    table[x2+1][y1] -= d

for i in range(n+1):
    for j in range(1, m+1):
        table[i][j] += table[i][j-1]

for i in range(m):
    for j in range(1, n+1):
        table[j][i] = table[j-1][i] 

