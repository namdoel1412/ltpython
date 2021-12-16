n = int(input())
for i in range(n):
    str = input()
    length = len(str)
    if str[0] == str[length-2] and str[1] == str[length - 1]:
        print('YES')
    else:
        print('NO')
