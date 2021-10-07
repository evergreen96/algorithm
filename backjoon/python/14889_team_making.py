import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

table = []
for _ in range(n):
    table.append(list(map(int,input().split())))

ret = int(1e9)
for value in combinations(range(1,n+1), n//2):
    rr = set(range(1, n+1))
    rr = rr - set(value)
    
    t1 = 0
    for v in rr:
        for w in rr:
            t1 += table[v-1][w-1]
    t2 = 0
    for v in value:
        for w in value:
            t2 += table[v-1][w-1]
    
    tmp = abs(t1-t2)

    if tmp < ret:
        ret = tmp

print(ret)