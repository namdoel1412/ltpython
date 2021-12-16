P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    inp = input()
    lst = inp.split(' ')
    k = int(lst[0])
    if k == 0:
        break
    str = lst[1]
    for i in str[::-1]:
        indx = P.find(i)
        print(P[(indx + k)%28], end='')
    print()