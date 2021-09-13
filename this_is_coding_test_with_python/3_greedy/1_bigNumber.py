n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()

first = data[-1]

second = data[-2]

cnt = (m//(k+1)) * k
cnt += m%(k+1)
remain = m - cnt

print((first * cnt) + (remain * second))
