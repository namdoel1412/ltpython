def isPrime(n):
    if n < 2:
        return False
    square = int(n**0.5)
    res = True
    for i in range(2, square+1):
        if n%i==0:
            res = False
    return res

def ucln(a, b):
    while(a > 0):
        tmp = a
        a = b%a
        b = tmp
    return b
        

n = int(input())
line = input()
lst = line.split(' ')
length = len(lst)
for i in range(length):
    lst[i] = int(lst[i])
lst.sort()
for i in range(n):
    for j in range(i+1, n):
        if ucln(lst[i], lst[j]) == 1:
            print(int(lst[i]), end=' ')
            print(int(lst[j]))



