import sys
from collections import deque
input = sys.stdin.readline


N = int(input())


def solution():
    n,k = map(int, input().split())
    times = [0]
    times += list(map(int,input().split()))
    degree = [0]* (n+1)
    graph = [[] for _ in range(n+1)]
    dp = [0] * (n+1)
    
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
    
    v = int(input())
    
    q = deque()
    flag = False
    for i in range(1, n+1):
        if degree[i]==0:
            if i==v:
                print(times[v])
                return
            q.append(i)
            dp[i] = times[i]
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            degree[next] -= 1
            dp[next] = max(dp[next], dp[now] + times[next])
            if degree[next]==0:
                q.append(next)
    print(dp[v])


for _ in range(N):
    solution()