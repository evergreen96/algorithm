from collections import deque
n, m, k, x = map(int, input().split(' '))

graph = [[] for _ in range(n+1)]



for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distances= [-1]*(n+1)
distances[x] = 0

def bfs():
    q = deque()
    q.append(x)

    while q:
        now = q.popleft()
        for v in graph[now]:
            if distances[v]==-1:
                distances[v] = distances[now]+1
                q.append(v)

bfs()
flag = False
for idx,value in enumerate(distances):
    if value==k:
        print(idx)
        flag = True

if not flag:
    print('-1')


