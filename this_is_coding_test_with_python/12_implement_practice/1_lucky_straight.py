n = input()

a ,b = n[ : (len(n)//2)], n[(len(n)//2):]

sa,sb = 0,0

for i in a:
    sa += int(i)
for i in b:
    sb += int(i)

if sa==sb:
    print("LUCKY")
else:
    print("READY")

