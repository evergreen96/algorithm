import sys
input = sys.stdin.readline

n,m = map(int, input().split())

visited = [0]*n
graph = [[]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag= False


def dfs(now, depth):
    global flag
    if depth==5:
        flag=True
        return 

    for next in graph[now]:
        if visited[next]==0:
            visited[next]= 1
            dfs(next, depth+1)
            visited[next] = 0

    return flag
    

for i in range(n):
    visited = [0]*n
    visited[i] = 1
    if dfs(i, 1):
        print(1)
        exit()

print(0)
