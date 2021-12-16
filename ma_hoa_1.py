t = int(input())
for item in range(t):
    tmp = input()
    num = 1
    length = len(tmp)
    lst = []
    for i in range(length - 1):
        if tmp[i] == tmp[i+1]:
            num+=1
        else:
            print(num, end='')
            print(tmp[i], end='')
            num=1
    print(num, end='')
    print(tmp[length-1])


