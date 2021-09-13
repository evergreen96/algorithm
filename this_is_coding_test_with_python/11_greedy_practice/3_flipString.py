s = input()

result = 1
first = now = s[0]

for v in s[1:]:
    if now != v:
        result += 1
        now = v

print((result//2))
        
