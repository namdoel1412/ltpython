while(True):
    t = int(input())
    if t == 0:
        break
    lst = []
    for i in range(0, t):
        lst.append(int(input()))
    length = len(lst)
    lst = sorted(lst)
    if lst[0] == lst[length -1]:
        print('BANG NHAU')
    else:
        print(lst[0], end=' ')
        print(lst[length - 1])