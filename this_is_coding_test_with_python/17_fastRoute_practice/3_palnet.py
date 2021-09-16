import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x< y:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())

xtable = []
ytable = []
ztable = []

tree = [0] * n

for i in range(n):
    tree[i] = i

for i in range(n):
    x,y,z  = map(int, input().split())
    xtable.append((x, i))
    ytable.append((y, i))
    ztable.append((z, i))

xtable.sort()
ytable.sort()
ztable.sort()

edges = []

for i in range(n-1):
    edges.append([xtable[i+1][0] -xtable[i][0],xtable[i][1],xtable[i+1][1]])
    edges.append([ytable[i+1][0] -ytable[i][0],ytable[i][1],ytable[i+1][1]])
    edges.append([ztable[i+1][0] -ztable[i][0],ztable[i][1],ztable[i+1][1]])


edges.sort()
total = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(tree, a) != find_parent(tree,b):
        union_parent(tree, a,b)
        total += cost

print(total)