t = int(input())

def ucln(a: int, b: int):
    while(b > 0):
        tmp = a
        a = b
        b = tmp%b
    return a

def isPrime(a: int):
    if a == 1: return False
    square = int(a**0.5) + 1
    for i in range(2, square):
        if a%i == 0:
            return False
    return True

for i in range(t):
    lst = [int(i) for i in input().split()]
    a = lst[0]
    b = lst[1]
    res = str(ucln(a, b))
    sum = 0
    for i in res:
        sum+=int(i)
    if isPrime(sum):
        print('YES')
    else:
        print('NO')

