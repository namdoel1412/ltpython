t = int(input())

def checkvalid(inp):
    length = len(inp)
    tmp = int(length/2)+1
    for i in range(0, tmp):
        if abs(ord(inp[i]) - ord(inp[i+1])) != abs(ord(inp[length-i-1]) - ord(inp[length-i-2])):
            return False
    return True

for i in range(0, t):
    inp = input()
    if checkvalid(inp):
        print('YES')
    else:
        print('NO')