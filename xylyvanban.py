res = ""
while True:
    try: 
        str2 = input() 
        res += str2 + " " 
    except EOFError: 
        break
length = len(res)
lst = []
tmp = ""
res = res.lower()
for i in range(0, length):
    if res[i] == '.' or res[i] == '?' or res[i] == '!':
        lst.append(tmp)
        tmp = ""
    else:
        tmp+=res[i]
for item in lst:
    tmp2 = str(item).strip()
    subList = tmp2.split()
    len2 = len(subList)
    for j in range(0, len2):
        if j == 0:
            print(subList[j].capitalize(), end='')
        else:
            print(subList[j], end='')
        if(j < len2-1):
            print(' ', end='')
    print()

