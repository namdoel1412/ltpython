def isPrime(n):
    if n < 2:
        return False
    square = int(n**0.5)
    res = True
    for i in range(2, n):
        if n%i==0:
            res = False
    return res

line1 = input().split()
n = int(line1[0])
m = int(line1[1])
lst = []
for i in range(n):
    line = input().split()
    lst.append(line)
for i in lst:
    for j in i:
        if isPrime(int(j)):
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()



