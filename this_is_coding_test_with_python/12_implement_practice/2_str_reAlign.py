
n = input()

start = ord('A')
end = ord('Z')

al= [ ]
di = [ ]

for v in n:
    vv  = ord(v)
    if start <= vv <= end:
        al.append(v)
    else:
        di.append(v)

al.sort()
di = sum(list(map(int, di)))
print(di)
al.append(str(di))
print(''.join(al))