import sys
from collections import deque
from collections import defaultdict
from itertools import permutations
input = sys.stdin.readline

n = int(input())
table = []
for _ in range(n):
    table.append(input().rstrip())

alpha = defaultdict(int)
for value in table:
    for i in range(len(value)):
        alpha[value[i]] += 10**(len(value)-1-i)

alpha = sorted(alpha.items(), key= lambda x:x[1], reverse=True)


total = 0
for i, value in enumerate(alpha):
    total += value[1] * (9-i)

print(total)
