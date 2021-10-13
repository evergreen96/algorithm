import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = []
for _ in range(n):
    table.append(list(input().rstrip()))

def show():
    for i in range(n):
        print(table[i])


def break_mineral(i,h):
    if i%2==0:
        for i in range(m):
            if table[h][i]=="x":
                table[h][i] = '.'
                break
    else:
        for i in range(m-1,-1,-1):
            if table[h][i]=="x":
                table[h][i] = '.'
                break

def check_mineral(h):
    pass
            

t = int(input())
heigh = list(map(int, input().split()))
for i, h in enumerate(heigh):
    h = n - h
    break_mineral(i, h)
    check_mineral(h)


show()

"""
5 6
......
..xx..
..x...
..xx..
.xxxx.
1
3

8 8
........
........
...x.xx.
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxx..x.
5
6 6 4 3 1
"""