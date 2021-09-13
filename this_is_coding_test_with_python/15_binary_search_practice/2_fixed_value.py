n = int(input())

nums = list(map(int, input().split()))
start=0
end = n-1

while start<=end:
    mid  = (start+end)//2
    if mid==nums[mid]:
        print(mid)
        exit()
    elif nums[mid]> mid:
        end = mid-1
    else:
        start = mid+1

print(-1)