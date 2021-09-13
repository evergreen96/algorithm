import sys

input = sys.stdin.readline

n = int(input())

result = []

for _ in range(n):
    a,b,c,d = input().split()
    result.append([a, int(b), int(c), int(d)])

result = sorted(result, key= lambda x :(-x[1], x[2], -x[3], x[0]))

for v in result:
    print(v[0])