import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)

table = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    table[a][b]  = min(table[a][b], c)


for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j==k:
                table[j][k]=0
            else:
                table[j][k] = min(table[j][k], table[j][i]+table[i][k])

for i in range(1, n+1):
    for j in range(1, n+1): 
        if table[i][j]==INF:
            print(0,end = ' ')
        else:
            print(table[i][j],end=' ')
    print()

"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""