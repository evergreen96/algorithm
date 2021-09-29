import sys
input = sys.stdin.readline

n = int(input())

table = []

for _ in range(n):
    table.append(list(map(int,input().split())))

cache = [[0]*(1<<n) for _ in range(n)]

fin = (1<<(n))-1
MAX = int(1e9)

def TSP(cur, visit):
    if fin==visit:
        if table[cur][0]==0:
            return MAX
        else:
            return table[cur][0]

    ret = cache[cur][visit]
    if ret !=0:
        return ret
    ret = MAX
    for i in range(1, n):
        if visit & (1<<i) == 0 and table[cur][i] !=0:
            ret = min(ret, TSP(i, visit | (1<<i)) + table[cur][i])
    
    cache[cur][visit]=ret
    return ret

print(TSP(0,1))


"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""