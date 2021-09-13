n = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

result = 1

for k in arr:
    if result < k:
        break
    else:
        result +=k
print(result)
