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


v, m = map(int, input().split())
parent = [0] * (v+1)

for i in range(0, v+1):
    parent[i] = i


for _ in range(m):
    a, b, c = map(int, input().split())
    if a==0:
        union_parent(parent, b, c)
    else:
        if find_parent(parent, b)==find_parent(parent,c):
            print("yes")
        else:
            print("no")