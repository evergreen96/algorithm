
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))


def binarySearch(arr, value, start, end):
    if start > end:
        return "No"
    
    mid = (start+end)//2
    if arr[mid]==value:
        return "Yes"
    else:
        if arr[mid]> value:
            return binarySearch(arr, value, start, mid-1)
        else:
            return binarySearch(arr,value, mid+1, end)


for i in x:
    print(binarySearch(arr,i,0,n-1))
