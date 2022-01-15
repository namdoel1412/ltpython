def UCNLN(a, b):
    while(b > 0):
        tmp = a%b
        a = b
        b = tmp
    return a

t = int(input())
for i in range(0, t):
    a = int(input())
    b = int(input())
    print(UCNLN(a, b))
