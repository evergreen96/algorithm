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

n = int(input())
table = [0] * (n+1)


for i in range(n):
    table[i] = i

p = int(input())

for _ in range(p):
    t = int(input())
    r = find_parent(table, t)
    if r==0:
        break
    union_parent(table, r, r-1)

    