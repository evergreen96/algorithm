
def update(tree, x, y, value):
    while x<len(tree):
        ty = y
        while(ty<len(tree[0])):
            tree[x][ty] += value
            ty += (ty&-ty)
        
        x += (x & -x)

def sum(tree, x, y):
    ret = 0
    while(x>0):
        ty = y
        while ty > 0:
            ret += tree[x][ty]
            ty -= (ty&-ty)
        
        x -= (x & -x)
    return ret

