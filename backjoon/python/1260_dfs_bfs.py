import sys
from collections import deque
input = sys.stdin.readline


n,m,k = map(int,input().split())

visited_d= [0] * (n+1)
visited_b = [0] * (n+1)
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    if b not in arr[a]:
        arr[a].append(b)
    if a not in arr[b]:
        arr[b].append(a)

for i in range(1, n+1):
    arr[i].sort()

visited_d[k] = 1
def dfs(now):
    print(now, end=' ')
    for next in arr[now]:
         if visited_d[next]==0:
            visited_d[next]=1
            dfs(next)

dfs(k)
print()


pipe = deque()
pipe.append(k)
visited_b[k]=1
while pipe:
    now = pipe.popleft()
    print(now, end=' ')


    for next in arr[now]:
        if visited_b[next]==0:
            visited_b[next]=1
            pipe.append(next)



"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""