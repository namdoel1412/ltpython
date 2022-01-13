def is_prime(num):
    if num < 2:
        return False
    tmp = int(num**0.5)+1
    for i in range(2, tmp):
        if num%i==0:
            return False
    return True

def check_valid(inp):
    length = len(inp)
    num1 = int(inp[0]+inp[1]+inp[2])
    num2 = int(inp[length-3] + inp[length-2] + inp[length-1])
    if(is_prime(num1) and is_prime(num2)):
        return True
    return False

n = int(input())
for i in range(0, n):
    inp = input()
    if(check_valid(inp)):
        print('YES')
    else:
        print('NO')