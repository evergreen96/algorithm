n = int(input())

table = []

for _ in range(n):
    table.append(list(map(int, input().split())))

result = [0]*(n+1)

old_time = table[0][0]
old_fee = table[0][1]
result[1] = old_fee
cnt = old_time-1

