n = int(input())
for i in range(n):
    str = input()
    tmp = len(str)
    for i in range(0, tmp-1, 2):
        for j in range(0, int(str[i+1])):
            print(str[i], end='')
    print('\n', end='')