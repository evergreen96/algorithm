from collections import deque
import copy
v = int(input())
indegree = [0] * (v+1)
times = [0] * (v+1)
graph = [[] for _ in range(v+1)]


for i in range(1, v+1):
    data = list(map(int, input().split()))
    times[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology():
    q = deque()
    result = copy.deepcopy(times)

    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+times[i])
            indegree[i] -= 1
            if indegree[i]==0:
                q.append(i)


    print(result)

topology()
