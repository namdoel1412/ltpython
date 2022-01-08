def is_prime(inp):
    value = int(inp)
    if value < 2: return False
    tmp = int(value**0.5)
    for i in range(2, tmp+1):
        if value%i == 0:
            return False
    return True

n = int(input())
for i in range(0, n):
    tmp = input()
    res = ''
    length = len(tmp)
    if length > 4:
        for j in range(length-4, length):
            res += tmp[j]
    else:
        res = tmp
    if is_prime(res):
        print('YES')
    else:
        print('NO')
    