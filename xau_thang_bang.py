t = int(input())
for i in range(t):
    str = input()
    length = len(str)
    res = []
    tmp = True
    for j in range(length-1):
        res.append(abs(ord(str[j]) - ord(str[j+1])))
    lenRes = len(res)
    for j in range(int(lenRes/2)):
        if res[j] != res[lenRes-j-1]:
            tmp = False
    if tmp == True:
        print('YES')
    else:
        print('NO')