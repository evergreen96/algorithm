s = input()

result = 0
for v in s:
    if int(v)==0 or result==0:
        result +=int(v)
    else:
        result *=int(v)


print(result)