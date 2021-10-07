import sys
input = sys.stdin.readline

n = int(input())

table = list(input().split())
visit = [False]*10

def check(num1, num2, sign):
    if sign == "<":
        return num1<num2
    if sign ==">":
        return num1>num2
    return True

ma = -1
mi = 10000000000

def solution(cnt, ss):
    global ma
    global mi
    if cnt==n+1:
        tmp = int(ss)
        tmp2 = int(ma)
        tmp3 = int(mi)

        if  tmp2 < tmp:
            ma = ss
        if  tmp3 > tmp:
            mi = ss
        return

    for v in range(10):
        if visit[v]==False:
            if cnt==0 or check(int(ss[-1]),v, table[cnt-1]):
                visit[v]=True
                solution(cnt+1, ss+str(v))
                visit[v]=False



solution(0, "")
print(ma)
print(mi)