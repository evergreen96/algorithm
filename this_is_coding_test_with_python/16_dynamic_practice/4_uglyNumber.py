
table = []

table[0] = 1
table[1] = 2
table[2] = 3


for i in range(4, int(1e9)):
    if len(table)==1000:
        break
    a,b,c = i/2, i/3, i/5
    if a in table:
        table.append(i)
    elif b in table:
        table.append(i)
    elif c in table:
        table.append(i)

n = int(input())

print(table[n])
    

