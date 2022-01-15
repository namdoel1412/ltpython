def valid(a):
    rev = a[::-1]
    num = int(a)
    i = 1
    while(i <= 1000 and num%7!=0):
        num += int(str(num)[::-1])
    return num


t = int(input())
for i in range(0, t):
    n = input()
    print(valid(n))
