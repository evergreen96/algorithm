n  = int(input())

table = []

table = [[0,0]]
result = [0]*(n+1)

for i in range(1, n+1):
    a,b = map(int, input().split())
    table.append((a,b))
    result[i] = b

for i in range(2, n+1):
    for j in range(1, i):
        if (i-j) >= table[j][0]:
            result[i] = max(result[i], result[j]+table[i][1])

mv = 0
for i in range(1, n+1):
    if i + table[i][0] <= n+1:
        if mv < result[i]:
            mv =  result[i]
        

print(mv)
