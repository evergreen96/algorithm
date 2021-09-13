n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n%k == 0:
        n /= k
    else :
        n -= 1
    cnt += 1

print(cnt)

# more efficient
cnt = 0
while True:
    sub = (n//k) * k
    cnt += n - sub
    n = sub
    if n < sub:
        break
    cnt += 1
    n //= k

cnt += n-1
print(cnt)