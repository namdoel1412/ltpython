while True:
    str = input()
    lst = []
    res = 0
    for item in str.split(' ', -1):
        lst.append(int(item))
    if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[3] == 0:
        break
    while True:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]:
            print(res)
            break
        else:
            res+=1
        first = lst[0]
        for i in range(0, 3):
            lst[i] = abs(lst[i] - lst[i+1])
        lst[3] = abs(lst[3] - first)
