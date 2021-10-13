import sys
input = sys.stdin.readline

n,l = map(int, input().split())

table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

rtable = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rtable[i][j] = table[j][i]

total = 0
def check(matrix):
    global total
    for row in matrix:
        cnt = len(set(row))
        if cnt==1:
            total += 1
        else:
            cnt = 1
            prev = row[0]
            flag = True
            for cur in row[1:]:
                if cur-prev == 1:
                    if cnt>=l:
                        prev = cur
                        cnt = 1
                    else:
                        flag = False
                        break
                elif prev-cur == 1:
                    if cnt >=0:
                        cnt = -l+1
                        prev = cur
                    else:
                        flag = False
                        break
                elif prev-cur==0:
                    cnt += 1
                else:
                    flag = False
                    break
            if flag and cnt>=0:
                total +=1


check(table)
check(rtable)

print(total)

"""
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2
"""