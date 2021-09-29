import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

table = [[0]*(n+1) for _ in range(n+1)]
graph = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    table[a][b] = table[b][a] = 1
    graph[a].append(b)
    graph[b].append(a)
total  = 0 


def dfs(now):
    """
    for idx in range(1, n+1):
        if table[now][idx] !=0 and visited[idx]==0:
            visited[idx]=1
            dfs(idx)
    """
    for next in graph[now]:
        if visited[next]==0:
            visited[next]=1
            dfs(next)

for i in range(1, n+1):
    if visited[i]==0:
        total += 1
        visited[i] = 1
        dfs(i)

print(total)

"""
6 5
1 2
2 5
5 1
3 4
4 6
"""