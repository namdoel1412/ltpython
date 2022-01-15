def UCLN(a, b):
    while(b > 0):
        tmp = a%b
        a = b
        b = tmp
    return a

arr = [int(i) for i in input().split()]
ms = int((arr[1]*arr[3])/UCLN(arr[1], arr[3]))

tick1 = int(ms/arr[1])
tick2 = int(ms/arr[3])

ts = tick1*arr[0] + tick2*arr[2]

tmp = UCLN(ts, ms)
print(int(ts/tmp), end='/')
print(int(ms/tmp))







