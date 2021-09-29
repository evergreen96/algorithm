import sys
input = sys.stdin.readline


n,m = map(int, input().split())

table = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    tmp = [0]
    tmp += list(map(int, input().split()))
    table[i+1] = tmp

for i in range(n+1):
    for j in range(1, m+1):
        table[i][j] += table[i][j-1]

for i in range(m+1):
    for j in range(1, n+1):
        table[j][i] += table[j-1][i]


k = int(input())

for _ in range(k):
    x1,y1, x2,y2 = map(int, input().split())
    a = table[x2][y2]
    b = table[x2][y1-1]
    c = table[x1-1][y2]
    d = table[x1-1][y1-1]
    print(a-b-c+d)