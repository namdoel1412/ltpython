t = int(input())

def checkvalid(inp):
    length = len(inp)
    for i in range(0, length):
        if inp[i] != '0' and inp[i] != '1' and inp[i] != '2':
            return False
    return True

for i in range(0, t):
    n = input()
    if checkvalid(n):
        print('YES')
    else:
        print('NO')