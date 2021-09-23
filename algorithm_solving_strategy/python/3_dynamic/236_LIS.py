import sys
input = sys.stdin.readline
N = int(input())

A,B = 0,0
table_A = []
table_B = []

def j_lis(matrix, idx_a, idx_b):
    global A
    global B
    global table_A
    global table_B
    v =  matrix[idx_a+1][idx_b+1]
    if (v!= -1):
        return v
    
    cnt = 2
    if idx_a==-1:
        aa = -int(1e9)
    else:
        aa = table_A[idx_a]
    if idx_b ==-1:
        bb = -int(1e9)
    else:
        bb = table_B[idx_b]
    mv = max(aa,bb)
    for next_a in range(idx_a+1, A):
        if mv < table_A[next_a]:
            cnt = matrix[idx_a+1][idx_b+1] = max(cnt, 1+ j_lis(matrix,next_a, idx_b))
    for next_b in range(idx_b+1, B):
        if mv < table_B[next_b]:
            cnt= matrix[idx_a+1][idx_b+1] = max(cnt, 1+ j_lis(matrix,idx_a, next_b))
    return cnt

def solution():
    global A
    global B
    global table_A
    global table_B
    A,B = map(int, input().split())
    table_A = list(map(int, input().split()))
    table_B = list(map(int, input().split()))
    matrix = [[-1]*(B+1) for _ in range(A+1)]
    print(j_lis(matrix, -1, -1)-2)





for _ in range(N):
    solution()


"""
1
5 3
10 20 30 1 2
10 20 30

3
3 3
1 2 4
3 4 7
3 3
1 2 3
4 5 6
5 3
10 20 30 1 2
10 20 30
"""