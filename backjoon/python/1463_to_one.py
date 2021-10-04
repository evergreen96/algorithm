import sys
sys.setrecursionlimit(10**6)
n = int(input())

table = [0]*(10000001)
table[2] = 1
table[3] = 1

if n<=3:
    print(table[n])
    exit()

for i in range(4, n+1):
    a= table[i//3] if i%3==0 else int(1e9)
    b = table[i//2] if i%2==0 else int(1e9)
    c = table[i-1]

    table[i] = min(a,b,c) + 1

print(table[n])


"""
def dp(now):
    if now<=3:
        return table[now]
    
    ret = table[now]
    if ret !=0:
        return ret
    
    a = int(1e9)
    if now%3==0:
        a = dp(now//3)
    b = int(1e9)
    if now%2 ==0:
        b = dp(now//2)
    c = dp(now-1)
    ret = table[now] = min(a,b,c)+1
    return ret
    print(dp(n))
"""




