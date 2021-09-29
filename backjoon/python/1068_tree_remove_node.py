import sys
input = sys.stdin.readline
n = int(input())

table = list(map(int,input().split()))
k = int(input())

"""
table[k] = -999

for _ in range(n):
    for i in range(0, n):
        if table[i] >0 and table[table[i]]==-999:
            table[i]=-999

"""
def dfs(idx):
    table[idx] = -999

    for i, p in enumerate(table):
        if p == idx:
            dfs(i)

dfs(k)

total = 0

for i in range(n):
    if table[i] != -999 and (i not in table):
        total += 1


print(total)

