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
        if a%i==0:
            return False
    return True

for i in range(t):
    inp = int(input())
    num = 1
    square = inp**0.5 + 1
    for j in range(2, inp):
        if ucln(j, inp) == 1:
            num+=1
    if isPrime(num):
        print('YES')
    else:
        print('NO')