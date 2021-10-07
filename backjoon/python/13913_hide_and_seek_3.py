from collections import deque
import heapq
n, k = map(int, input().split())

end = 100000
visited = [-1]*(end+1)
def bfs(n, k):
    #q =deque()
    q = []
    q.append((0, n))
    visited[n] = n
    while q:
        time, now = heapq.heappop(q)
        if now==k:
            print(time)
            break
            
        n1, nt1 = now*2, time+1
        n2, nt2 = now+1, time+1
        n3, nt3 = now-1, time+1

        if n1<=end and visited[n1]==-1:
                visited[n1] = now
                #q.append((nt1, n1))
                heapq.heappush(q, (nt1, n1))
        if n2<=end and visited[n2]==-1:
                visited[n2] = now
                #q.append((nt2, n2))
                heapq.heappush(q, (nt2,n2))
        if n3>=0 and visited[n3]==-1:
                visited[n3] = now
                #q.append((nt3, n3))
                heapq.heappush(q, (nt3,n3))

if n > k:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end= ' ')
else:
    bfs(n, k)
    idx = k
    result = deque()
    while True:
        result.appendleft(idx)
        if idx==n:
            break
        idx = visited[idx]
    print(' '.join(map(str, result)))

"""
5 17
"""