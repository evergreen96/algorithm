import sys
input = sys.stdin.readline
N = int(input())
MV = int(1e9)

switch = [
    [0,1,2],
    [3,7,9,11],
    [4,10,14,15],
    [0,4,5,6,7],
    [6,7,8,10,12],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15],
    [1,2,3,4,5],
    [3,4,5,9,13]
]


def nextTime(table, psitions, direction):
    for v in psitions:
        table[v] += (3*direction)
        if table[v] > 12:
            table[v] -= 12
        elif table[v] < 0:
            table[v] += 12
    return table


def check(table):
    for v in table:
        if v != 12:
            return False
    return True

def dfs(table, start, cnt):
    if check(table):
        return cnt

    value = MV
    for i in range(start, 10):
        postions = switch[i]
        for j in range(4):
            table = nextTime(table, postions, 1)
            value = min(value, j+dfs(table,i+1, cnt+1))
    
    return value

def solution():
    table = list(map(int,input().split()))
    result = MV
    result = dfs(table, 0, 0)
    if result !=MV:
        print(result)
    else:
        print(-1)


for _ in range(N):
    solution()

"""
2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6

1
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
1
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6
"""