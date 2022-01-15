def UCLN(a, b):
    while(b > 0):
        tmp = a%b
        a = b
        b = tmp
    return a

arr = [int(i) for i in input().split()]
ucln = UCLN(arr[0], arr[1])
print(int(arr[0]/ucln), end='/')
print(int(arr[1]/ucln))


