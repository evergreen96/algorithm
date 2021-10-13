import sys
input = sys.stdin.readline

s, n = map(int, input().split())

col, row = 2*s+3, s+2 

def init():
    tmp = [[' ']*row for _ in range(col)]
    return tmp

def draw(table, digit):
    if digit==0:
        for i in range(col):
            if i in (0 ,col-1):
               table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i != s+1:
                    table[i][0] = table[i][-1] = "|"
    if digit==1:
        for i in range(col):
            if i not in (0, s+1 ,col-1):
               table[i][-1] = "|"
    if digit == 2:
        for i in range(col):
            if i in (0, s+1 ,col-1):
                table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i < s+1:
                    table[i][-1] = "|"
                else:
                    table[i][0] = '|'  
    if digit ==3:
        for i in range(col):
            if i in (0, s+1 ,col-1):
                table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                    table[i][-1] = "|"
    if digit ==4:
        for i in range(col):
            if i in (0, s+1 ,col-1):
                if i==s+1:
                    table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i < s+1:
                   table[i][0] =  table[i][-1] = "|"
                else:
                    table[i][-1] = '|'  
    if digit == 5:
        for i in range(col):
            if i in (0, s+1 ,col-1):
                table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i > s+1:
                    table[i][-1] = "|"
                else:
                    table[i][0] = '|'  
    if digit == 6:
        for i in range(col):
            if i in (0, s+1 ,col-1):
                table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i < s+1:
                    table[i][0] = "|"
                else:
                    table[i][0] = table[i][-1] = '|'  
    if digit==7:
        for i in range(col):
            if i not in (0, s+1 ,col-1):
               table[i][-1] = "|"
            elif i == 0:
                table[i] = [' '] + ['-']*(row-2) + [' ']
    if digit==8:
        for i in range(col):
            if i in (0, s+1 ,col-1):
               table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i != s+1:
                    table[i][0] = table[i][-1] = "|"
    if digit == 9:
        for i in range(col):
            if i in (0, s+1 ,col-1):
                table[i] = [' '] + ['-']*(row-2) + [' ']
            else:
                if i < s+1:
                    table[i][0] = table[i][-1] = "|"
                else:
                    table[i][-1] = '|'     

result = []
for digit in str(n):
    table = init()
    draw(table,int(digit))
    result.append(table)


for i in range(2*s+3):
    for j in range(len(result)):
        print(''.join(result[j][i]), end=' ')
    print()

"""
2 1234567890
"""