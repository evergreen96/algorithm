
# select sort
arr = [5,8,4,7,3,2,1,0,9,6]
for i in range(len(arr)-1):
    idx = i
    for j in range(i+1, len(arr)):
        if arr[idx] > arr[j]:
            idx = j
    
    arr[idx], arr[i] = arr[i], arr[idx]

print(arr)

# insert sort
arr = [5,8,4,7,3,2,1,0,9,6]
for i in range(1, len(arr)):
    for j in range(i, 0 ,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)

# quick sort

arrq = [9,8,4,7,3,2,1,0,5,6]

def quick(arr, start, end):
    print(arr)
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end

    while left<=right:
        while left<=end and arr[left]<=arr[pivot]:
            print('=')
            left +=1
        while right > start and arr[right]>=arr[pivot]:
            print('-')
            right -= 1
        
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quick(arr, start,right-1)
    quick(arr, right+1, end)

quick(arrq, 0, len(arrq)-1)
print(arrq)


"""
arr = [0,0,0,3,4,4,7,8,9,9,0,9,6,6,6,4,3]

count = [0]*(max(arr)+1)

for v in arr:
    count[v] += 1

for i,v in enumerate(count):
    for j in range(v):
        print(i, end='')
"""