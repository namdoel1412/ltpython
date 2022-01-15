t = int(input())
def check(inp):
    length = len(inp)
    if length < 6 or length > 12:
        return False
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(0, length):
        if str(inp[i]).islower():
            count1+=1
        if str(inp[i]).isupper():
            count2+=1
        if str(inp[i]).isdigit():
            count3+=1
        if inp[i] == '$' or inp[i] == '#' or inp[i] == '@':
            count4+=1
    if count1 > 0 and count2 > 0 and count3 > 0 and count4 > 0:
        return True
    return False

res = []
for i in range(0, t):
    lst = input().split(',')
    for item in lst:
        if(check(item)):
            res.append(item)

length = len(res)
# for i in range(0, length):
#     print(res[i], end='')
#     if i < length -1:
#         print(',', end='')
# print()

for i in range(0, length):
    print(res[i])