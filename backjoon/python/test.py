import sys
input = sys.stdin.readline


n = int(input())

flag = False
if n < 0:
    n = -n
    flag = True

arr = [0]*(n+1)
arr[0] = '0'
arr[1] = '1'
arr[2] = '1T'
arr[3] = '10'


up = n
tmp = ''
while up > 3:
    re = up%3
    up = up//3
    if re == 2:
        tmp ='T' + tmp
        up += 1
    else:
        tmp =str(re) + tmp
tmp = arr[up] + tmp

        
if not flag:
    print(tmp)
else:
    p = ''
    for v in tmp:
        if v=='1':
            p +='T'
        elif v=='T':
            p+='1'
        else:
            p +='0'
    print(p)


"""
3
iabucdpefcg
"""