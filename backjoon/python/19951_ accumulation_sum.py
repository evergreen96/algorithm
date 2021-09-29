"""
10 3
1 2 3 4 5 -1 -2 -3 -4 -5
1 5 -3
6 10 5
2 7 2
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

table = list(map(int, input().split()))
pile  = [0] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    pile[a-1] += c
    pile[b] += -c

for i in range(1, n):
    pile[i] += pile[i-1]

for i in range(n):
    table[i] += pile[i]
    
    
for i in range(n):
    print(table[i], end=' ')
print()


