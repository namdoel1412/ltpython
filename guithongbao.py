t = int(input())
for i in range(0, t):
    inp = input()
    length = len(inp)
    if length <= 100:
        print(inp)
    else:
        tmp = ''
        res = ''
        for j in range(0, 100):
            tmp += inp[j]
        k = 99
        while((ord(tmp[k]) >= ord('a') and ord(tmp[k]) <= ord('z')) or (ord(tmp[k]) >= ord('A') and ord(tmp[k]) <= ord('Z'))):
            k-=1
        #print(k)
        for j in range(0, k+1):
            res += tmp[j]
        print(res)

            
        