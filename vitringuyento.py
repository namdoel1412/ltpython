def is_prime(inp):
    value = int(inp)
    if value < 2:
        return False
    tmp = int(value**0.5)
    for i in range(2, tmp+1):
        if value%i==0:
            return False
    return True

n = int(input())
for i in range(0, n):
    tmp = input()
    length = len(tmp)
    res = 0
    for j in range(0, length):
        if (is_prime(j) == False and is_prime(tmp[j]) == True) or (is_prime(j) == True and is_prime(tmp[j]) == False):
            print('NO')
            res = 1
            break
    if res == 0:
        print('YES')
