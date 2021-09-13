n = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
group = []
for i,v in enumerate(arr):
    group.append(v)
    if len(group) == v:
        cnt += 1
        group = []


print(cnt)