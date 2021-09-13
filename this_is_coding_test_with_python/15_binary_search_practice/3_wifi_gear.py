n, c = map(int, input().split())

table = []

for _ in range(n):
    table.append(int(input()))

table.sort()

start = 1
end = table[-1] - table[0]

result = 0

while start<= end:
    mid = (start+end) // 2
    
    left = table[0]
    cnt = 1
    
    for i in range(1, n):
        if table[i] >= left + mid:
            left = table[i]
            cnt += 1
    
    if cnt >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1


print(result)