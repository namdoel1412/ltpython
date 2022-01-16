inp = input()

def binToOct(inp):
    length = len(inp)
    res = 0
    for i in range(length-1, -1, -1):
        if inp[i] == '1':
            res+=pow(2, length - i -1)
    return res

length = len(inp)
bonus = length%3
if bonus != 0:
    for i in range(0, 3-bonus):
        inp = '0'+inp
length = len(inp)
res = ''
for i in range(0, length, 3):
    res += str(binToOct(inp[i]+inp[i+1]+inp[i+2]))
print(res)
