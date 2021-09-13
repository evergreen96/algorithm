from collections import deque
n,m  = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 0, 1, 0]    
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < n and 0<= ny <m and graph[nx][ny] != 0:
                if graph[nx][ny]==1:
                    graph[nx][ny] = graph[qx][qy] + 1
                    q.append((nx,ny))

    return graph[n-1][m-1]
print(bfs(0,0))