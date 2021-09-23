c = int(input())


def dfs(table, visited):
    position = -1
    for i, v in enumerate(visited):
        if v == 0:
            position = i
            break
    if position==-1:
        return 1
    
    result = 0
    for i in range(position+1, len(visited)):
        if visited[i]==0 and table[position][i] == 1:
            visited[position] = visited[i]= 1
            result += dfs(table, visited)
            visited[position] = visited[i] = 0

    return result

def solution():
    n,m = map(int, input().split())
    table  =[[0]*(n) for _ in range(n)]
    visited = [0]*(n)
    ins  = list(map(int, input().split()))

    for i in range(0,len(ins),2):
        a,b = ins[i], ins[i+1]
        table[a][b] = table[b][a] = 1

    total = dfs(table, visited)
    print(total)

for _ in range(c):
    solution()