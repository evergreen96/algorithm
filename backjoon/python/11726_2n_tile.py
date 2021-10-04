n = int(input())

table = [0] *(n+1)
table[1] = 1
table[2] = 2
table[3] = 3
for i in range(4, n+1):
    table[i] = table[i-1] + table[i-2]

print(table[n]%10007)