c = int(input())


def solution():
    n, l = map(int, input().split())
    table = list(map(int, input().split()))
    result = 0
    mv = float('inf')
    result = []
    for x in range(n-l+1):
        total = 0
        cnt = 1
        for y in range(x, n):
            total += table[y]
            if cnt >= l:
                tmp = total/cnt
                if mv > tmp:
                    mv = tmp
            cnt += 1
    print("%.8f"%mv)






for _ in range(c):
    solution()
