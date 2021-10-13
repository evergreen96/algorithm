import sys

input = sys.stdin.readline

T = int(input())

table = []
for _ in range(T):
    tmp = list(map(str, input().rstrip()))
    table.append(list(map(int,tmp)))


n = int(input())

def check_left(num):
    if num<0:
        return False
    if table[num][2] != table[num+1][6]:
        return True
    else:
        return False

def check_right(num):
    if num>=T:
        return False
    if table[num][6] != table[num-1][2]:
        return True
    else:
        return False


def rot_right(num, dir):
    if check_right(num):
        rot_right(num+1, -dir)
        rot(num, dir)

def rot_left(num ,dir):
    if check_left(num):
        rot_left(num-1, -dir)
        rot(num, dir)


def rot(num, dir):
    if dir==1:
        table[num] = [table[num][-1]] + table[num][:-1]
    else:
        table[num] = table[num][1:] + [table[num][0]]


for _ in range(n):
    num, dir = map(int, input().split())
    rot_right(num, -dir)
    rot_left(num-2, -dir)

    rot(num-1, dir)

    

total = 0
for i in range(T):
    total += table[i][0]

print(total)

"""
4
10101111
01111101
11001110
00000010
2
3 -1
1 1
"""