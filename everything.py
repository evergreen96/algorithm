import sys
n = int(input())

table = [0]*10001

for _ in range(n):
    table[int(input())] += 1

for i,v in enumerate(table):
    for _ in range(v):
        print(i)