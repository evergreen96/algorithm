n  = int(input())

table = []

for _ in range(n):
    table.append(list(map(int, input().split())))


result = [[] for _ in range(n)]

result[0] = [table[0][0]]

for i in range(1, n):
    for j in range(i+1):
            if j==0:
                a = 0
            else:
                a = table[i-1][j-1]
            
            if j==i:
                b = 0
            else:
                b = table[i-1][j]

            table[i][j] = table[i][j] + max(a, b)    


print(max(table[n-1]))