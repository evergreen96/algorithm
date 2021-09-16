import random
"""
n = int(input())
table = list(map(int, input().split()))
"""
n = 6
table = [1,7,3,9,2,7]

result = [1] * n

for i in range(1, n):
    for j in range(i):
        if table[i] < table[j] and result[i] < result[j]+1:
            result[i] = result[j]+1

print(result)
print(n-max(result))