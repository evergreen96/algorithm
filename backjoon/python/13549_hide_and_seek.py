from collections import deque
import heapq
n, k = map(int, input().split())

end = 100000
visited = [0]*(end+1)

def bfs(n, k):
    q = []
    q.append((0, n))
    visited[n] = 1

    while q:
        time, now = heapq.heappop(q)
        if now==k:
            print(time)
            exit()
        
        n1, nt1 = now*2, time
        n2, nt2 = now+1, time+1
        n3, nt3 = now-1, time+1

        if n1<=end and visited[n1]==0:
            visited[n1] = 1
            heapq.heappush(q, (nt1, n1))
        
        if n2<=end and visited[n2] ==0:
            visited[n2] = 1
            heapq.heappush(q, (nt2, n2))
        
        if n3>=0 and visited[n3]==0:
            visited[n3] =1
            heapq.heappush(q, (nt3, n3))

bfs(n,k)

"""
5 17
"""