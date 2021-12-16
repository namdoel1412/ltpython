t = int(input())
for i in range(t):
    tmp = input()
    length = len(tmp)
    res = ''
    du = 0
    #lst = [range(length-1, 0)]
    #print(lst)
    for j in range(length-1, 0, -1):
        if int(tmp[j])+du >= 5:
            res='0'+res
            du = 1
            #print('bigger')
        else:
            du = 0
            res='0'+res
            #print('smaller')
    res = str(int(tmp[0])+du) + res
    print(res)
        

    