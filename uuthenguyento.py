def is_prime(num):
    if num < 2:
        return False
    tmp = int(num**0.5)+1
    for i in range(2, tmp):
        if num%i == 0:
            return False
    return True

def check_valid(inp):
    length = len(inp)
    primeNums = 0
    for i in range(0, length):
        if is_prime(int(inp[i])):
            primeNums+=1
    if is_prime(length) and primeNums > length/2:
        return True
    return False

n = int(input())
for i in range(0, n):
    inp = input()
    if check_valid(inp):
        print('YES')
    else:
        print('NO')