import sys
input = sys.stdin.readline
N = int(input())

substr = []

def flip():
    global substr
    if substr[0]=="w" or substr[0]=="b":
        tmp = substr[0]
        substr = substr[1:]
        return [tmp]
        
    substr = substr[1:]
    lu = flip()
    ru = flip()
    ld = flip()
    rd = flip()

    return ["x"]+ld+rd+lu+ru
    

def solution():
    global substr
    substr = list(input().rstrip())
    print(''.join(flip()))



for _ in range(N):
    solution()

"""
1
xbwwb
4
w
xbwwb
xbwxwbbwb
xxwwwbxwxwbbbwwxxxwwbbbwwwwbb
"""