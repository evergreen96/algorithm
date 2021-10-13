import sys
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))
m = int(input())
commands = []
for _ in range(m):
    commands.append(list(map(int, input().split())))

matrix = [[0]*(n) for _ in range(n)]

for i in range(n):
    matrix[i][i] = 1

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if table[i]==table[j]:
            if matrix[i+1][j-1]==1:
                matrix[i][j] = 1
            if j==i+1:
                matrix[i][j]=1
            

for i in range(n):
    print(matrix[i])


for left, right in commands:
    print(matrix[left-1][right-1])

"""
def check_valid(start, end):
    for i in range(start, (start+end)//2 + 1):
        if table[i] != table[end+start-i]:
            return False
    return True

for i in range(n):
    for j in range(i):
        if check_valid(j, i):
            dp[i].add(j)


for (left, right) in commands:
    if left-1 in dp[right-1]:
        print(1)
    else:
        print(0)   

""" 

"""
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
"""