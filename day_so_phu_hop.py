t = int(input())
for i in range(0, t):
    n = int(input())
    str = input()
    str2 = input()
    lst = []
    for item in str.split():
        lst.append(int(item))
    lst.sort()
    lst2 = []
    for j in str2.split():
        lst2.append(int(j))
    lst2.sort()
    res = True
    #print(lst)
    #print(lst2)
    for k in range(0, n):
        if lst[k] > lst2[k]:
            res = False
            break
    if res == True:
        print("YES")
    else:
        print("NO")

# T = int(input())
# for t in range(T):
#     n = int(input())
#     arr1 = list(int(i) for i in input().split())
#     arr2 = list(int(i) for i in input().split())
#     arr1.sort()
#     arr2.sort()
#     check = 'YES'
#     for i in range(0, n):
#         if arr1[i] > arr2[i]:
#             check = 'NO'
#             break
#     print(check)