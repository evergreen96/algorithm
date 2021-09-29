def sum(tree, i):
    ret = 0
    while(i>0):
        ret += tree[i]
        i -= (i & -i)
    
    return ret

def update(tree, i, value):
    while(i < len(tree)):
        tree[i] += value
        i += (i & -i)


n,m,k = map(int, input().split())
arr = [0]*(n+1)
tree = [0]*(n+1)
for i in range(1,n+1):
    value = int(input())
    arr[i] = value
    update(tree, i, value)

