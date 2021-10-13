import sys
input = sys.stdin.readline

n = int(input())
dcol = [0, -1, 0, 1]
drow = [1, 0, -1, 0]

table = [[0]*101 for _ in range(101)]



for _ in range(n):
    row, col, dir, g = map(int, input().split())
    table[col][row] = 1
    q = [dir]
    for _ in range(g):
        tmp = []
        for v in q[::-1]:
            tmp.append((v+1)%4)
        q.extend(tmp)
    for d in q:
        col = col + dcol[d]
        row = row + drow[d]
        table[col][row] = 1


total = 0

for i in range(100):
    for j in range(100):
        if table[i][j] + table[i+1][j] + table[i][j+1] + table[i+1][j+1] == 4:
            total += 1


print(total)



"""4
3
3 3 0 1
4 2 1 3
4 2 2 1
"""