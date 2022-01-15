t = int(input())

def checkvalid(inp):
    length = len(inp)
    for i in range(0, length-2, 2):
        if inp[i] != inp[i+2]:
            return False
    for i in range(1, length-2, 2):
        if inp[i] != inp[i+2]:
            return False
    
    return True


for i in range(0, t):
    n = input()
    if checkvalid(n):
        print('YES')
    else:
        print('NO')
    

