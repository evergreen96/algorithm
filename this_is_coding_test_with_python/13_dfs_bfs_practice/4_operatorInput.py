from itertools import permutations, product
from collections import deque
import copy, sys
#input = sys.stdin.readline

INF = int(1e9)
n = int(input())
numbers = list(map(int, input().split()))
add_op, sub_op, mul_op, div_op = map(int, input().split())

minV = INF
maxV = int(-1e9)

def dfs(cnt , now):
    global add_op, sub_op, mul_op, div_op, minV, maxV
    if cnt==n:
        minV = min(minV, now)
        maxV = max(maxV, now)
    else:
        if add_op >0:
            add_op -= 1
            dfs(cnt+1, now+numbers[cnt])
            add_op += 1
        if sub_op > 0:
            sub_op -= 1
            dfs(cnt+1, now-numbers[cnt])
            sub_op += 1
        if mul_op > 0:
            mul_op -= 1
            dfs(cnt+1, now*numbers[cnt])
            mul_op += 1
        if div_op > 0:
            div_op -=1
            dfs(cnt+1, int(now/numbers[cnt]))
            div_op +=1 

dfs(1, numbers[0])

print(maxV)
print(minV)


""" 틀린답
from itertools import permutations
from collections import deque
INF = int(1e9)
n = int(input())
numbers = list(map(int, input().split()))
opernums = list(map(int, input().split()))
operators = ''
for v in range(len(opernums)):
    if v==0:
        operators +='+'*opernums[v]
    elif v==1:
        operators +='-'*opernums[v]
    elif v==2:
        operators +='*'*opernums[v]
    else:
        operators +='%'*opernums[v]

operlist = list(permutations(operators))
maxValue = -INF
minValue = INF
for op in operlist:
    q = deque(numbers)
    for i  in range(n-1):
        a, b = q.popleft(), q.popleft()
        tool = op[i]
        if tool=="+":
            q.appendleft(a+b)
        elif tool=="-":
            q.appendleft(a-b)
        elif tool=="*":
            q.appendleft(a*b)
        else:
            q.appendleft(int(a/b))
    
    result = q.pop()
    if maxValue < result:
        maxValue = result
    if minValue > result:
        minValue = result

print(maxValue)
print(minValue)


"""