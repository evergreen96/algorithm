
data = input()
row = int(data[1])
col =  ord(data[0])- 97 + 1


moves = [(-2, -1), (-1, 2), (1, -2), (2, -1),(2, 1),(1, 2), (-1 ,2), (-2, 1)]

cnt = 0
for move in moves:
    nr = row + move[0]
    nc = col + move[1]

    if 1<=nr<=8 and 1<=nc<=8:
        cnt +=1
print(cnt)