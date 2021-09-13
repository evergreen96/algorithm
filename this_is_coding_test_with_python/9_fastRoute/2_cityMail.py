import heapq
INF = int(1e9)
n,m,start = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))


def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for nx, nd in graph[now]:
            cost = dist + nd
            if cost < distance[nx]:
                distance[nx] = cost
                heapq.heappush(q,(cost, nx))

dijk(start)

count = 0
max_dist = 0

for v in distance:
    if v !=INF:
        count += 1
        max_dist = max(max_dist, v)

print(count-1, max_dist)
