import sys
input = sys.stdin.readline

T = int(input())

def divider(table, start, end):
    if start >= end:
        return table[start]
    
    mid = (start+end)//2
    left = divider(table, start, mid)
    right = divider(table, mid+1, end)

    area = max(left, right)

    ll = mid; rr = mid+1
    height = min(table[ll], table[rr])

    area = max(area, height*2)

    while start< ll or end>rr:
        if rr<end and ((table[ll-1]< table[rr+1] or ll==start)):
            rr+=1
            height = min(height, table[rr])
        else:
            ll -= 1
            height = min(height, table[ll])
        
        area = max(area, height*(rr-ll+1))
    return area

    



def solution():
    n = int(input())
    table = list(map(int,input().split()))
    print(divider(table, 0, n-1))

for _ in range(T):
    solution()

"""

1
7
7 1 5 9 6 7 3

3
7
7 1 5 9 6 7 3
7
1 4 4 4 4 1 1
4
1 8 2 2

"""