t = int(input())

def checkvalid(num):
    inp = str(num)
    if inp != inp[::-1]:
        return False
    length = len(inp)
    if length % 2 != 0:
        return False
    for i in range(0, length):
        if int(inp[i])%2!=0:
            return False
    return True

for i in range(0, t):
    n = int(input())
    for i in range(22, n, 2):
        if checkvalid(i):
            print(i, end=' ')
    print()