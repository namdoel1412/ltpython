t = input()
length = len(t)
num4 = 0
num7 = 0
for i in t:
    if i == '4':
        num4+=1
    elif i == '7':
        num7+=1
if num7+num4 == 4 or num7+num4 == 7:
    print('YES')
else:
    print('NO')
