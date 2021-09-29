
import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

def solution():
    v, e = map(int,input().split())
    graph = [[]*(v+1) for _ in range(v+1)]

    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (v+1)

    for i in range(1, v+1):
        if visit[i]==0:
            q = deque()
            visit[i] = 2
            q.append((i,2))
            if bfs(q, graph, visit) == False:
                print("NO")
                return
    print("YES")




def bfs(q:deque, graph, visit):
    while q:
        now, depth = q.popleft()
        add = -1
        if depth%2==0:
            add  = 1

        for next in graph[now]:
            if visit[next] == 0:
                visit[next] = depth+add
                q.append((next, depth+add))
            elif visit[next] == depth:
                return False
    
    return True
    


for _ in range(k):
    solution()


"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
"""