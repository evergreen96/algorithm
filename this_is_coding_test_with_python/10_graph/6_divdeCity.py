def find_parent(parent, x):
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


 
v, e = map(int, input().split())
parent = [0] * (v+1)


edges = []
result = 0


for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

maxlen = 0

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        maxlen = cost

print(result, maxlen)
print(result-maxlen)

