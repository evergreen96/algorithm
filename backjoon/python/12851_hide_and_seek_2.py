from collections import deque
import heapq
n, k = map(int, input().split())

end = 100000
visited = [0]*(end+1)
ret = 0
fast = 10000000
def bfs(n, k):
    global ret
    global fast
    q = deque()
    q.append((0, n))
    visited[n] = 1

    while q:
        time, now = q.popleft()

        if now==k:
            if fast > time:
                fast = time
            ret += 1
        n1, nt1 = now*2, time+1
        n2, nt2 = now+1, time+1
        n3, nt3 = now-1, time+1

        if n1<=end:
            if visited[n1]==0 or visited[n1]>time:
                visited[n1] = time+1
                q.append((nt1, n1))
        
        if n2<=end:
            if visited[n2]==0 or visited[n2]>time:
                visited[n2] = time+1
                q.append((nt2, n2))
        
        if n3>=0:
            if visited[n3] == 0 or visited[n3] >time:
                visited[n3] = time+1
                q.append((nt3, n3))

bfs(n,k)
print(fast)
print(ret)
"""
5 17
"""