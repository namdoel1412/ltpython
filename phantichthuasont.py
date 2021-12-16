t = int(input())
for i in range(t):
    req = int(input())
    i = 2
    dict = {}
    # if req == 1:
    #     print(1)
    #     continue
    while(req != 1):
        if req%i == 0:
            req/=i
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        else:
            i+=1
    print('1', end='')
    for item in dict.items():
        print(' * ', end='')
        print(str(item[0])+'^'+str(item[1]), end='')
    print()
