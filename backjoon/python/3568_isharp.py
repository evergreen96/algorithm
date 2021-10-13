import sys
input = sys.stdin.readline


ipt = input().split()

for i in range(1, len(ipt)):
    tmp = ipt[i]
    result = ipt[0]
    for j in range(len(tmp)-2, 0, -1):
        if tmp[j].isalpha():
            break
        elif tmp[j]=="[":
            result += ']'
        elif tmp[j]=="]":
            result += '['
        else:
            result += tmp[j]
    result += ' '
    for j in range(len(tmp)):
        if tmp[j].isalpha():
            result += tmp[j]

    result +=';'
    print(result)