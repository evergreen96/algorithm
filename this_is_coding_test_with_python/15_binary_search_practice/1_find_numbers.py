from bisect import bisect_left, bisect_right

n, k = map(int, input().split())
nums = list(map(int, input().split()))

cnt = bisect_right(nums, k) - bisect_left(nums, k)
print(cnt)


def findLeft(start , end):
    global k
    if start> end:
        return -1
    else:
        mid  = (start + end)//2
        if nums[mid]==k:
            if mid==0 or nums[mid-1] != k:
                return mid
            else:
                end = mid-1
                return findLeft(start, end)
        else:
            if nums[mid] < k:
                start = mid + 1
                return findLeft(start, end)
            else:
                end = mid-1
                return findLeft(start, end)

def findRight(start , end):
    global k
    if start> end:
        return -1
    else:
        mid  = (start + end)//2
        if nums[mid]==k:
            if mid+1==len(nums) or nums[mid+1] != k:
                return mid
            else:
                start = mid+1
                return findRight(start, end)
        else:
            if nums[mid] > k:
                end = mid-1
                return findRight(start, end)
            else:
                start = mid+1
                return findRight(start, end)


a,b = findLeft(0, len(nums)-1), findRight(0, len(nums)-1)
print(b-a+1)