from collections import deque

v, e = map(int, input().split())

indgree = [0] * (v+1)
graph = [[] for _ in range(v+1)]


for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indgree[b] += 1

def topolgy_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indgree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for idx in graph[now]:
            indgree[idx] -= 1

            if indgree[idx]==0:
                q.append(idx)

    print(result)

topolgy_sort()
