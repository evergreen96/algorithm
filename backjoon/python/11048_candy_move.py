import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
table = []
table.append([0]*(M+1))

for _ in range(N):
    tmp = [0] + list(map(int, input().split()))
    table.append(tmp)

visit = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        visit[i][j] = table[i][j] + max(visit[i-1][j], visit[i][j-1], visit[i-1][j-1])

print(visit[N][M])


"""
3 4
1 2 3 4
0 0 0 5
9 8 7 6
"""