t = int(input())
for i in range(t):
    tmp = int(input())
    step = 2
    for j in range(22, tmp, step):
        if(len(str(j))%2 != 0):
            step = 10**(len(str(j))+1) - j
        else:
            ant = str(j)
            rev = ant[::-1]
            if ant == rev:
                check = True
                for item in ant:
                    if int(item)%2!=0:
                        check = False
                        break
                if check == True:
                    print(ant, end=' ')
            step = 2
    print()
        