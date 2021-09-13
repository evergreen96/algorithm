from collections import deque
import heapq
import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    stack.append(int(input()))


if len(stack)==1:
    print(stack[0])
    exit()

result = 0
heapq.heapify(stack)

for _ in range(n-1):
   a, b = heapq.heappop(stack), heapq.heappop(stack)
   tmp = a+b
   heapq.heappush(stack, tmp)
   result += tmp

print(result)
