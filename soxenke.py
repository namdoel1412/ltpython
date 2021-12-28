def check(inp):
    length = len(inp)
    if(length%2==0):
        return False
    if(inp[0] == inp[1]):
        return False
    for j in range(0, length-2, 2):
        if(inp[j] != inp[j+2]):
            return False
    return True

n = int(input())
for i in range(0, n):
    num = input()
    if(check(num)):
        print('YES')
    else:
        print('NO')