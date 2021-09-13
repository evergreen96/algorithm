from itertools import combinations
import heapq
n , m = map(int, input().split())
arr = list(map(int, input().split(' ')))

heapq.heappop

values = combinations(arr, 2)

cnt = 0
for x, v in values:
    if x != v:
        cnt += 1

print(cnt)


######################

arr.sort()
values = [0] * 11

for a in arr:
    values[a] += 1

result = 0

for i in range(1, m+1):
    n -= values[i]
    result += n* values[i]

print(result)

