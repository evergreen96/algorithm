import sys
from collections import deque
input = sys.stdin.readline

n  = int(input())


def solution():
    a = int(input())
    table = list(map(int, input().split()))
    graph = [[]*(a+1) for _ in range(a+1)]
    indegree = [0] *(a+1)
    
    for i, v in enumerate(table):
        for t in table[i+1:]:
            graph[t].append(v)
            indegree[v] += 1
     

    b = int(input())

    for _ in range(b):
        x,y = map(int, input().split())
        if y in graph[x]:
            graph[x].remove(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] -= 1
        else:
            graph[y].remove(x)
            graph[x].append(y)
            indegree[x] -=1
            indegree[y] +=1

    result = []
    q = deque()


    for i in range(1, a+1):
        if indegree[i]==0:
            q.append(i)
            break
    

    while q:
        v = q.popleft()
        result.append(v)

        for ne in graph[v]:
            indegree[ne] -= 1
            if indegree[ne]==0:
                q.append(ne)
        
    if len(result)==a:
        print(*list(reversed(result)))
        return
    else:
        print("IMPOSSIBLE")

for _ in range(n):
    solution()

"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3

1
5
5 4 3 2 1
2
2 4
3 4

1
4
1 2 3 4
3
1 2
3 4
2 3
"""