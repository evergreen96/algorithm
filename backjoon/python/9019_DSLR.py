import sys
from collections import deque
input = sys.stdin.readline

n = int(input())


def D(num):
    return ((2*num) % 10000)

def S(num):
    return 9999 if num==0 else num-1

def L(num):
    return (num%1000)*10 + (num//1000)

def R(num):
    return (num%10)*1000 + (num//10)


def solution():
    start, end = map(int, input().split())
    visit = [False]*10000
    q = deque()
    q.append((start, ''))
    visit[start] = True
    while q:
        num,path = q.popleft()
        if num==end:
            print(path)
            break
        nd = D(num)
        if visit[nd]==False:
            visit[nd] = True
            q.append((nd, path+"D"))

        ns = S(num)
        if visit[ns]==False:
            visit[ns] = True
            q.append((ns, path+"S"))
        
        nl = L(num)
        if visit[nl]==False:
            visit[nl] = True
            q.append((nl, path+"L"))

        nr = R(num)
        if visit[nr] == False:
            visit[nr] = True
            q.append((nr, path+"R"))




for _ in range(n):
    solution()
    


"""
3
1234 3412
1000 1
1 16
"""