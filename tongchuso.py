def tongCS(inp):
    length = len(inp)
    res = 0
    for i in range(0, length):
        res += int(ord(inp[i])-ord('0'))
    return str(res)

inp = input()
length = len(inp)
result = 0
if len(inp) == 1:
    result = 1
while(len(inp) > 1):
    inp = tongCS(inp)
    result+=1
print(result)



