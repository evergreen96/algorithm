import sys
input = sys.stdin.readline

"""
1
12341234 


5 
12341234 
11111222 
12122222 
22222222 
12673939
"""


N = int(input())
table = []
cach = []
def solution():
    global table
    global cach
    table = list(input())[:-2]
    table = list(map(int, table))
    cach = [-1] * len(table)
    print(mesmerize(0))

def mesmerize(idx):
    global table, cach
    if idx >= len(table):
        return 0
    
    ret = cach[idx]
    if ret != -1:
        return ret
    
    ret = int(1e9)
    for i in range(3, 6):
        if i+idx <= len(table):
            ret = min(ret, mesmerize(idx+i)+score(table[idx:idx+i]))
            cach[idx] = ret
    
    return ret

def score(sub_nums):
    L = len(sub_nums)
    is_same = True
    for i in range(1,L):
        if sub_nums[0]!=sub_nums[i]:
            is_same=False
            break
    if is_same:
        return 1
    
    is_seq = True
    seq_num = 0
    for i in range(1, L-1):
        seq_num = sub_nums[i]-sub_nums[i-1]
        if (sub_nums[i]-sub_nums[i-1]) != (sub_nums[i+1]-sub_nums[i]):
            is_seq=False
            break
    
    if is_seq and (seq_num== -1 or seq_num==1):
        return 2
    
    is_alter = True
    for i in range(2, L):
        if sub_nums[i] != sub_nums[i%2]:
            is_alter=False
            break
    
    if is_alter:
        return 4
    
    if is_seq:
        return 5

    return 10
    
    

    



for _ in range(N):
    solution()
